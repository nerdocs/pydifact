from typing import Callable, Dict, List, Tuple, Union

from edi_energy import EDISegment, EDIenergy


def ensure_str(iterable) -> list:
    """Ensures all elements of an iterable are strings.

    First checks the types of all elements in given iterable.
    If more types or no str is given, convert them.

    Parameters
    ----------
    iterable : _type_
        _description_

    Returns
    -------
    list

    """
    # get unique types
    types = set(type(t) for t in iterable)

    # check all elements are strings, else convert them
    if len(types) > 1 or types.pop() is not str:
        iterable = list(i if type(i) is str else str(i) for i in iterable)

    return iterable


def check_type_of(val) -> str:
    """Verifies type of val is str and returns it or raises Error.

    Parameters
    ----------
    val : any
        value to verify

    Returns
    -------
    str
        val

    Raises
    ------
    TypeError
        if type of val is not str
    """
    if type(val) is not str:
        raise TypeError(
            f"Comparing {type(val)} to the index is currently not supported."
        )

    return val


class Index:
    def __init__(self, index: Union[list, dict]) -> None:
        if not type(index) in (list, dict):
            raise TypeError(f"{type(index)=} is not supported as whitelist")

        self.has_info = False

        if isinstance(index, dict):
            self.has_info = True
            # override method name
            self.check = self.check_dict

            self.index = dict(zip(ensure_str(index.keys()), ensure_str(index.values())))
        else:
            self.index = ensure_str(index)

    def check(self, id) -> bool:
        """Check if id is in index"""
        return id in self.index

    def check_dict(self, id) -> Union[Tuple[bool, str], bool]:
        """Check if id is in index and return stored info if true."""
        is_present = id in self.index
        return (is_present, self.index[id]) if is_present else is_present

    def check_with_input_verification(self, id):
        """Wrapper to verify the given id, befor looking it up.

        Parameters
        ----------
        id : any
            id to look up

        """
        return self.check(check_type_of(id))


def index_check_base_str(id: Union[str, int], count: int, in_index: bool) -> str:
    return f"ID-Code: {id}\t count: {count}\t whitelisted: {in_index}\n"


def index_check_with_info(id: Union[str, int], count: int, in_index: Tuple[bool, str]):
    return f"ID-Code: {id}\t count: {count}\t whitelisted: {in_index[0]}\t target: {in_index[1]}\n"


def compare_segments_to_index(
    edi_message: EDIenergy,
    class_edi_seg: EDISegment,
    index: Union[List, Dict, Index],
    predicate: Callable[[EDISegment], bool] = None,
) -> str:
    """Compare the values of specific segments to an index.



    Parameters
    ----------
    edi_message : EDIenergy
        message to analyze
    class_edi_seg : EDISegment
        a child class of type EDISegment
    index : Union[List, Dict, Index]
        a whitelist to compare to
    predicate : Callable[[EDISegment], bool]
        an optional segment qualifier to identify data segments,
        defaults to None, then all segments of this class will be evaluated

    Returns
    -------
    str
        result of comparison: 'ID-Code: 13025\t count: 1\t whitelisted: False\n'
    """

    if not isinstance(index, Index):
        index = Index(index)

    # choosing the str constructor method
    str_constructor = index_check_with_info if index.has_info else index_check_base_str

    # get segments and their values
    segments_with_tag = [
        seg for seg in edi_message.get_segments(class_edi_seg.tag, predicate=predicate)
    ]
    ids_of_segments = [class_edi_seg(seg).get() for seg in segments_with_tag]

    # create output str 
    output_str = []
    for id in set(ids_of_segments):

        output_str.append(
            str_constructor(
                id, sum(1 for i in ids_of_segments if i == id), index.check(id)
            )
        )

    return "".join(output_str)
