# Pydifact - a python edifact library
#
# Copyright (c) 2021 Karl Southern
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import collections
from copy import deepcopy
from typing import List, Tuple, Iterator

from pydifact.segmentcollection import Message
from pydifact.api import EDISyntaxError
from pydifact.segments import Segment as Seg, SegmentFactory


class BiDirectionalIterator:
    """
    Bi-directional iterator. Used as a convenience when parsing Message
    Segments.
    """

    def __init__(self, collection: List):
        self.collection = collection
        self.index = 0

    def __next__(self):
        try:
            result = self.collection[self.index]
            self.index += 1
        except IndexError:
            raise StopIteration
        return result

    def __prev__(self):
        self.index -= 1
        if self.index < 0:
            raise StopIteration
        return self.collection[self.index]

    def __getitem__(self, key):
        return self.collection[key]

    def next(self):
        """
        Alias for __next__ method.
        """
        return self.__next__()

    def prev(self):
        """
        Alias to __prev__ method.
        """
        return self.__prev__()

    def __iter__(self):
        return self


class AbstractMappingComponent:
    """
    Abstract EDIFact Component, used as a base for Segments, SegmentGroups,
    Loops
    """

    def __init__(self, **kwargs):
        self.mandatory = kwargs.get("mandatory", False)

    def from_segments(self, iterator: BiDirectionalIterator):
        """
        Convert a BiDirectionalIterator of Segment instances into this mapping
        component.
        """
        raise NotImplementedError()

    def to_segments(self) -> List[Seg]:
        """
        Converts a mapping component to a list of Segment.
        """
        raise NotImplementedError()

    # pylint: disable=no-self-use
    def validate(self) -> bool:
        """
        Mapping component validation.
        """
        return True

    @property
    def present(self) -> bool:
        """
        Is the mapping component present?
        """
        raise NotImplementedError()


class Segment(AbstractMappingComponent):
    """
    EDIFact Component.
    A simple wrapper for Segment
    """

    def __init__(self, tag: str, *elements, **kwargs):
        super(Segment, self).__init__(**kwargs)

        self.__component__ = SegmentFactory.create_segment(
            tag, *elements, validate=False
        )
        self.__present__ = True

    @property
    def tag(self) -> str:
        return self.__component__.tag

    def __str__(self) -> str:
        return "{} {}".format(type(self.__component__), str(self.__component__))

    def __getitem__(self, key):
        return self.__component__[key]

    def __setitem__(self, key, value):
        self.__component__[key] = value
        if not self.__present__:
            self.__present__ = True

    def validate(self) -> bool:
        return self.__component__.validate()

    def from_segments(self, iterator: BiDirectionalIterator):
        segment = iterator.next()

        if self.tag == segment.tag:
            self.__component__ = segment
            self.__present__ = True
            return

        if self.mandatory:
            raise EDISyntaxError("Missing %s, found %s" % (self.tag, segment))

        self.__present__ = False

        iterator.prev()

    def to_segments(self):
        return self.__component__

    @property
    def present(self) -> bool:
        return self.__present__


class SegmentGroupMetaClass(type):
    """
    Metaclass to maintain an ordered list of components.
    Required for compatibility with Python 3.5. In 3.6 the
    properties of a class are strictly ordered.
    """

    @classmethod
    def __prepare__(cls, _name, _bases):
        return collections.OrderedDict()

    def __new__(cls, name, bases, classdict):
        result = type.__new__(cls, name, bases, dict(classdict))
        exclude = set(dir(type))

        result.__components__ = []

        for k, v in classdict.items():
            if k not in exclude and isinstance(v, AbstractMappingComponent):
                result.__components__.append(k)
        return result


class SegmentGroup(AbstractMappingComponent, metaclass=SegmentGroupMetaClass):
    """
    Describes a group of AbstractMappingComponent
    """

    def from_segments(self, iterator: Iterator):
        icomponent = iter(self.__components__)

        try:
            while True:
                component_name = next(icomponent)
                component = getattr(self, component_name)
                component.from_segments(iterator)
        except StopIteration:
            pass

    def to_segments(self):
        segments = []

        for component_name in self.__components__:
            component = getattr(self, component_name)
            component_segments = component.to_segments()

            if isinstance(component_segments, list):
                segments += component_segments
            else:
                segments.append(component_segments)

        return segments

    def to_segment_dict(self) -> dict:
        seg_dict: dict = {}
        for component_name in self.__components__:
            component = getattr(self, component_name)
            if isinstance(component, Loop):
                component_segments = component.to_segment_dict()
                seg_dict[component_name] = component_segments
            else:
                component_segments = component.to_segments()
                seg_dict[component_name] = {}

                if isinstance(component_segments, list):
                    seg_dict[component_name]["tag"] = component_name
                    seg_dict[component_name]["elements"] = {}
                    for line_comp in component_segments:
                        seg_dict[component_name]["elements"]["tag"] = line_comp.tag
                        seg_dict[component_name]["elements"][
                            "elements"
                        ] = line_comp.elements
                else:
                    seg_dict[component_name]["tag"] = component_segments.tag
                    seg_dict[component_name]["elements"] = []

                    if isinstance(component_segments.elements, list):
                        seg_dict[component_name][
                            "elements"
                        ] = component_segments.elements
                    else:
                        seg_dict[component_name]["elements"].append(
                            component_segments.elements
                        )

        return seg_dict

    def from_message(self, message: Message):
        """
        Create a mapping from a Message.
        """
        iterator = BiDirectionalIterator(message.segments)
        self.from_segments(iterator)

    def to_message(self, reference_number: str, identifier: Tuple):
        """
        Convert this mapping component into a new Message
        """
        segments = self.to_segments()
        return Message.from_segments(reference_number, identifier, segments)

    def __str__(self) -> str:
        res = []
        for component_name in iter(self.__components__):
            component = getattr(self, component_name)
            res.append(str(component))
        return "\n".join(res)

    @property
    def present(self) -> bool:
        return any(
            getattr(self, component_name).present
            for component_name in self.__components__
        )


def deepcopy_obj(obj_in):
    """Quick hack to deepcopy an object in a loop. Otherwise, reading the 2nd
    loop object would overwrite the data read in at the first loop operation.
    """
    obj_out = deepcopy(obj_in)
    for comp_name in iter(obj_in.__components__):
        component = getattr(obj_in, comp_name)
        new_comp = deepcopy(component)
        setattr(obj_out, comp_name, new_comp)
    return deepcopy(obj_out)


class Loop(AbstractMappingComponent):
    """
    Describes a repeating SegmentGroup
    """

    def __init__(self, component, **kwargs):
        super(Loop, self).__init__(**kwargs)
        self.min = kwargs.get("min", 0)
        self.max = kwargs.get("max", 0)

        if self.mandatory and self.min < 1:
            self.min = 1

        if self.max < self.min:
            self.max = self.min

        self.__component__ = component
        self.value = []

    def from_segments(self, iterator: BiDirectionalIterator):
        # TODO: really bad hack to reset the deeply copied value list.
        # Occours if two EDI messages are parsed and the second one contains
        # more order items than the first. Then, the 2nd message will contain
        # the first's order items plus their own.
        self.value = []
        ##### hack end
        i = 0
        while i < self.max:

            try:
                component = self.__component__()
                component.from_segments(iterator)
                self.value.append(deepcopy_obj(component))
            except EDISyntaxError:
                iterator.prev()
                if self.mandatory and i < self.min:
                    raise EDISyntaxError("Missing %s" % (self.__component__.__name__))
                break

            i += 1

        if i < self.min:
            raise EDISyntaxError("Minimum required not met")

    def to_segments(self):
        segments = []

        for value in self.value:
            segments += value.to_segments()

        return segments

    def to_segment_dict(self) -> dict:
        seg_dict: dict = {}
        for idx, value in enumerate(self.value):
            seg_dict[idx] = value.to_segment_dict()

        return seg_dict

    def __str__(self) -> str:
        res = []
        for v in self.value:
            res.append(str(v))
        return "{} = {}".format(self.__component__.__name__, str(res))

    def __getitem__(self, key):
        return self.value[key]

    def __setitem__(self, key, value):
        self.value[key] = value

    def append(self, value: AbstractMappingComponent):
        """
        Append an item to the loop
        """
        self.value.append(value)

    @property
    def present(self) -> bool:
        return any(value.present for value in self.value)
