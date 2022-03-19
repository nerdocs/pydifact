"""
This module bundels all EDI@energy message formats.

Default EDIfact formats like ORDERS, MSCONS or UTILMD as well as derived ones
like ALOCAT or TSIMSG are implemented.

"""

import codecs
import datetime
from typing import Generator, Iterable, List, Tuple, Union

from pydifact.parser import Parser

from .energy_collections import EnergySegmentsContainer, LINGroup
from .energy_segments import CCI, DTM, IDE, LIN, LOC, NAD, PIA, RFF, UNB, EDISegment
from .errors import MessageError
from .segmentcollection import Interchange


class EDIenergy(Interchange):
    """
    EDI@Energy Messages are Edifact Interchanges which contain Messages.

    All Message Formats e.g. ORDERS, UTILMD, MSCONS or ORDRSP are constructed from
    an interchagen beteween UNB - UNZ tags, containing a message between BGM - UNS tags.
    Within are different segment groups...

    """

    START_TAG = "BGM"
    END_TAG = ""  # optional MSCONS don't have them

    BLOCK_TAG = ""
    BLOCK_TAG_END = ""

    def __init__(self, edi_message: Interchange = None, casted: bool = False) -> None:
        """creates an instance of class EDIenergy

        Args:
            edi_message (Interchange): _description_
            casted (bool, optional): True if construction of child classes. Defaults to False.
        """
        # create new, empty instance and add segments later
        if not edi_message:
            super().__init__("", "", "", ("", 0))
            return

        # constructs instance with equal attributes as given interchange obj
        for key, val in vars(edi_message).items():
            setattr(self, key, val)

        self.rff = [
            RFF(r).get() for r in self.get_segments(RFF.tag, flag=RFF.qualifier)
        ]

    def get_message_info(self) -> Tuple[str, str, datetime.datetime, str]:
        """returns the UNB header as readable tuple

        Implemented for convinience, because resetting the Interchange
        attributes conflicts with the reconstruction of the UNB header.


        Returns
        -------
        Tuple
            sender, recipient, timestamp, control_ref
        """
        unb = UNB(self.get_header_segment())
        return unb.sender, unb.recipient, self.timestamp, self.control_reference

    def get_header_block(self) -> EnergySegmentsContainer:
        """retuns a container for n extra header elements

        Returns
        -------
        EnergySegmentsContainer
           segments contianing all header segments
        """
        container = EnergySegmentsContainer()
        container.add_segment(self.get_header_segment())

        if self.extra_header_elements:
            return container.add_segments(self.segments[: self.extra_header_elements])

        return container

    def get_footer_block(self) -> EnergySegmentsContainer:
        """footer is cunstructed from END_TAG to last segment

        Returns
        -------
        EnergySegmentsContainer
            containing footer segments
        """
        container = EnergySegmentsContainer()

        if self.END_TAG:
            idx = self.get_first_index(self.END_TAG)
            extra_segments = self.segments[idx : len(self.segments) - 1]
            container.add_segments(extra_segments)

        return container.add_segment(super().get_footer_segment())

    @classmethod
    def from_segments(cls, segments: Union[list, Iterable]) -> "EDIenergy":
        """Create a new instance from a iterable list of segments.

        Parameters
        ----------
        segments : Union[list,Iterable]
            The segments of the EDI interchange

        Returns
        -------
        EDIenergy

        """
        return cls(super().from_segments(segments))

    @classmethod
    def from_str(cls, string: str) -> "EDIenergy":
        """Create an instance from a string.

        Parameters
        ----------
        string : str
            The EDI content

        Returns
        -------
        EDIenergy

        """

        segments = Parser().parse(string)

        # UNA, service segment is not part of the message
        edi_message = cls.from_segments(segments)
        edi_message.has_una_segment = string[0:3] == "UNA"

        return edi_message

    @classmethod
    def from_file(cls, file: str, encoding: str = "iso8859-1") -> "EDIenergy":
        """Create a Interchange instance from a file.

        Parameters
        ----------
        file : str
            The full path to a file that contains an EDI message.
        encoding : str, optional
            by default "iso8859-1"

        Returns
        -------
        EDIenergy

        Raises
        ------
        FileNotFoundError
        Lookup Error
            codec was not found
        """
        # codecs.lookup raises an LookupError if given codec was not found:
        codecs.lookup(encoding)

        with open(file, encoding=encoding) as f:
            collection = f.read()

        return cls.from_str(collection)

    def split_by_segment(
        self,
        segment_tag: str,
        end_tag: Union[str, Tuple[str, Union[str, int]]] = None,
    ) -> Generator[EnergySegmentsContainer, None, None]:
        """creates segment blocks divided by tags

        Parameters
        ----------
        segment_tag : str
            tag to split by
        end_tag : Union[str, Tuple[str, Union[str, int]]], optional
            end tag of block, by default None

        Yields
        ------
        Generator[EnergySegmentsContainer, None, None]
            of split blocks
        """
        for msg in self.get_messages():
            if end_tag:
                groups = msg.split_by(segment_tag, end_tag)
            else:
                groups = msg.split_by(segment_tag)
            for g in groups:
                yield g

    def get_with_block_tag(self) -> Generator[EnergySegmentsContainer, None, None]:
        """splits message by format block tag

        compare: split_by_segment()

        Returns
        -------
        Generator
            equal to obj.split_by_segment(obj.BOCK_TAG)

        Yields
        ------
        Generator[EnergySegmentsContainer, None, None]
            for split blocks

        Raises
        ------
        ValueError
            if EDIenergy has no BLOCK_TAG class attribute
        """
        if not self.BLOCK_TAG:
            raise ValueError("No block tag provided!")

        return self.split_by_segment(self.BLOCK_TAG, self.BLOCK_TAG_END)

    def get_lin_blocks_of_bc(
        self, balancing_group: str
    ) -> Generator[LINGroup, None, None]:
        """get LIN blocks of specific blanancing group

        Parameters
        ----------
        balancing_group : str
            to get LIN blocks of

        Yields
        ------
        Generator[LINGroup, None, None]
            containing the complete LIN Grou
        """
        for block in self.get_with_block_tag():
            for nad in block.get_segments(NAD.tag):
                nad = NAD(nad)
                if nad.qualifier == "ZEU":
                    if nad.get_id() == balancing_group:
                        yield block

    def pretty_print(self):
        """formatted output of underlying segments"""

        if self.BLOCK_TAG:
            print(self.get_header_block().serialize(True))
            for block in self.get_with_block_tag():
                print(block.serialize(True))

            print(self.get_footer_block().serialize(True))
        else:  # print rest
            print(self.serialize(True))

    def compare_whitelist_info(
        self, class_edi_seg: EDISegment, whitelist: List[str], flag: str = ""
    ):
        """check if given segment types are in whitelist

        Parameters
        ----------
        class_edi_seg : EDISegment
            a child class of type EDISegment
        whitelist : List[str]
            a whitelist to compare to
        flag : str
            an optional segment qualifier to identify data segments,
            defaults to "", then all segments of this class will be evaluated
        """
        # TODO verify whitelist is list[str]
        segments_with_tag = [
            seg for seg in self.get_segments(class_edi_seg.tag, flag=flag)
        ]
        ids_of_segments = [class_edi_seg(seg).get() for seg in segments_with_tag]
        for id in set(ids_of_segments):
            print(
                f"ID-Code: {id}\t count: {len([1 for i in ids_of_segments if i == id])}\t whitelisted: {id in whitelist}"
            )

    def check_segments_count(self):
        unt = self.get_segment("UNT")
        unt

    def print_info(self, with_dates: bool = True, segment_structure: List = []):

        output = []

        header = self.get_header_segment()
        footer = self.get_footer_segment()

        output.append(str(header))
        output.append("\n\n\t")

        if segment_structure:
            output.extend(segment_structure)
        else:
            output.extend(self._segment_structure(with_dates))

        output.append("\n")

        output.append(str(footer))
        output.append("\n\n")

        print("".join(output))

    def _segment_structure(self, with_dates: bool = True):
        nl = "\n\t\t"
        structure = []

        # TODO use this as input for a recursive split 'n info func
        # use enumerate to set indentaion lvl
        # _split_structure = {
        #   seg_to_split_by: info_to_add_at_this level,
        #   2n_lvl_split: (seg_class, optional_qualifier)
        #   3rd_lvl: (seg_class, (seg_class, qualifier)...),
        # }
        _structure = {
            "BGM": ((RFF, RFF.qualifier)),
            LIN.tag: (
                LIN,
                (LOC, "172"),
                (NAD, NAD.flag_balancing_group),
                (DTM, DTM.flag_137),
            ),
        }
        for bgm in self.split_by(self.START_TAG):

            container = EnergySegmentsContainer.from_segments(bgm.segments)

            rff = container.get_segments(RFF.tag, flag=RFF.qualifier)
            structure.extend([str(r) for r in rff])
            structure.append("\n\t")

            if container.get_segment(LIN.tag):
                segment_groups = container.split_by(LIN.tag)
            else:
                segment_groups = [container]

            for gr in segment_groups:

                lin = gr.get_segment(LIN.tag)
                loc = gr.get_segment(LOC.tag, flag="172")
                nad = gr.get_segment(NAD.tag, flag=NAD.flag_balancing_group)
                dtm = gr.get_segments(DTM.tag, flag=DTM.flag_137)

                info_segments = (lin, loc, nad)
                for e, el in enumerate(info_segments):
                    if el:
                        structure.append(str(el))
                    if el and e < len(info_segments) - 1:
                        structure.append(nl)
                    elif el and e == len(info_segments) - 1:
                        structure.append("\n\t")

                if with_dates:
                    # output.append(nl)
                    structure.extend(nl.join([str(d) for d in dtm]))
                # else:
                #     output.append("\n\t")
                # if with_dates:
                #     out = f"{header}\n\t{[str(r) for r in rff]}\n\t{loc}\n\t\t{nl.join([str(d) for d in dtm])}\n{footer}\n\n"
                # else:
                #     out = f"{header}\n\t{[str(r) for r in rff]}\n\t{loc}\n{footer}\n\n"
        return structure


class ORDRSP(EDIenergy):
    END_TAG = "UNS"

    BLOCK_TAG = "LIN"
    BLOCK_TAG_END = ("NAD", "ZSO")

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.validate()

        self.extra_header_elements = self.get_first_index(self.BLOCK_TAG)

    def validate(self):
        super().validate()
        messages = self.get_messages()

        if len([msg for msg in messages]) != 1:
            raise MessageError(f"{self.__class__} usally have only one message group!")

    @classmethod
    def from_file(cls, *args, **kwargs):
        interchange = super().from_file(*args, **kwargs)
        return cls(interchange)


class ALOCAT(ORDRSP):

    END_TAG = "UNS"

    BLOCK_TAG = "LIN"
    BLOCK_TAG_END = ("NAD", "ZSO")

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def validate(self):
        super().validate()
        # messages = self.get_messages()

        # if len([msg for msg in messages]) != 1:
        #     raise MessageError("Alocats usally have only one message group!")

    @classmethod
    def from_file(cls, *args, **kwargs):
        interchange = super().from_file(*args, **kwargs)
        return cls(interchange, casted=True)


class IMBNOT(ORDRSP):

    END_TAG = "UNS"

    BLOCK_TAG = "LIN"
    BLOCK_TAG_END = ("NAD", "ZSO")

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def validate(self):
        super().validate()
        # messages = self.get_messages()

        # if len([msg for msg in messages]) != 1:
        #     raise MessageError("Alocats usally have only one message group!")

    @classmethod
    def from_file(cls, *args, **kwargs):
        interchange = super().from_file(*args, **kwargs)
        return cls(interchange, casted=True)


class UTILMD(EDIenergy):
    """Exchange of base data and changes

    Parameters
    ----------
    EDIenergy :
        Base class of all EDIenergy messages
    """

    BLOCK_TAG = IDE.tag

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.validate()

        self.extra_header_elements = self.get_first_index(self.BLOCK_TAG)

        self.loc = [LOC(l).get() for l in self.get_segments(LOC.tag)]

    def validate(self):
        super().validate()
        messages = self.get_messages()

        # TODO add proper validation method!

    @classmethod
    def from_file(cls, *args, **kwargs):
        # TODO reading an empty file or corrupt msconfig leads to script errors
        # there fore a skip and warning message should be implemented!
        edi_interchange = super().from_file(*args, **kwargs)
        return cls(edi_interchange, casted=True)


class TSIMSG(UTILMD):
    """Deklarationslisten Gas

    für die Übermittlung Deklarationsliste nach dem BDEW/VKU-Leitfaden
    Geschäftsprozesse zur Führung und Abwicklung von Bilanzkreisen bei Gas

    Die TSIMSG basiert auf der UTILMD MIG in der jeweils aktuellsten von EDI@Energy
    veröffentlichten Version. Dieses Dokument beschreibt die Ausprägung der UTILMD für die
    Anwendungsfälle Deklarationsliste NB an MGV und MGV an BKV. Diese Anwendungsfälle werden
    als TSIMSG bezeichnet.
    Wenn in der TSIMSG für eine Fallgruppe ein Bilanzkreis im Betrachtungsmonat genannt ist und
    SG4 DTM+92 und SG4 DTM+93 sind vorhanden, wird diese deklariert. Sind für die in der TSIMSG
    genannte Fallgruppe und den genannten Bilanzkreis im Betrachtungsmonat sowohl SG4 DTM+92
    als auch SG4 DTM+93 nicht vorhanden, wird dadurch die Deklaration zurückgezogen.

    Args:
        EDIenergy (_type_): _description_
    """

    BLOCK_TAG = ""

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def validate(self):
        super().validate()
        # messages = self.get_messages()

        # if len([msg for msg in messages]) != 1:
        #     raise MessageError("TSIMSGs usally have only one message group!")

    @classmethod
    def from_file(cls, *args, **kwargs):
        interchange = super().from_file(*args, **kwargs)
        return cls(interchange, casted=True)

    @property
    def eic_codes(self):
        return [CCI(bk).get() for bk in self.get_segments(CCI.tag, flag=CCI.bk_flag)]


class MSCONS(EDIenergy):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.validate()

        self.extra_header_elements = self.get_first_index(self.BLOCK_TAG)

        self.loc = [LOC(l).get() for l in self.get_segments(LOC.tag)]
        self.pia = [PIA(p).get() for p in self.get_segments(PIA.tag)]

    def validate(self):
        super().validate()
        messages = self.get_messages()

        # TODO add proper validation method!

    @classmethod
    def from_file(cls, *args, **kwargs):
        # TODO reading an empty file or corrupt msconfig leads to script errors
        # there fore a skip and warning message should be implemented!
        interchange = super().from_file(*args, **kwargs)
        return cls(interchange, casted=True)

    def print_info(self, with_dates: bool = True):

        #     for msg in self.get_messages():
        #         header = msg.get_header_segment()
        #         footer = msg.get_footer_segment()

        #         rff = msg.get_segment(RFF.tag)
        #         loc = msg.get_segment(LOC.tag)
        #         dtm = msg.get_segments(DTM.tag)

        #         nl = "\n\t\t"

        #         if with_dates:
        #             out = f"{header}\n\t{rff}\n\t{loc}\n\t\t{nl.join([str(d) for d in dtm])}\n{footer}\n\n"
        #         else:
        #             out = f"{header}\n\t{rff}\n\t{loc}\n{footer}\n\n"

        #         print(out)
        nl = "\n\t\t"

        output = []

        for msg in self.get_messages():
            header = msg.get_header_segment()
            footer = msg.get_footer_segment()

            output.append(str(header))
            output.append("\n\n\t")

            for bgm in self.split_by(self.START_TAG):

                container = EnergySegmentsContainer.from_segments(bgm.segments)

                rff = container.get_segments(RFF.tag, flag=RFF.qualifier)
                output.extend([str(r) for r in rff])
                output.append("\n\t")

                if container.get_segment(NAD.tag):
                    segment_groups = container.split_by(
                        NAD.tag, start_segment_flag="DP"
                    )
                else:
                    segment_groups = [container]

                for gr in segment_groups:

                    lin = gr.get_segment(LIN.tag)
                    loc = gr.get_segment(LOC.tag, flag="172")
                    nad = gr.get_segment(NAD.tag, flag=NAD.flag_balancing_group)
                    dtm = gr.get_segments(DTM.tag, flag=DTM.flag_137)

                    info_segments = (lin, loc, nad)
                    for e, el in enumerate(info_segments):
                        if el:
                            output.append(str(el))
                        if el and e < len(info_segments) - 1:
                            output.append(nl)
                        elif el and e == len(info_segments) - 1:
                            output.append("\n\t")

                    if with_dates:
                        # output.append(nl)
                        output.extend(nl.join([str(d) for d in dtm]))
                    # else:
                    #     output.append("\n\t")
                    # if with_dates:
                    #     out = f"{header}\n\t{[str(r) for r in rff]}\n\t{loc}\n\t\t{nl.join([str(d) for d in dtm])}\n{footer}\n\n"
                    # else:
                    #     out = f"{header}\n\t{[str(r) for r in rff]}\n\t{loc}\n{footer}\n\n"

            output.append("\n")
            output.append(str(footer))
            output.append("\n\n")

            print("".join(output))
