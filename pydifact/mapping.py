import collections
import itertools
from typing import Callable, List, Optional, Tuple, Union

from pydifact.segmentcollection import Message
from pydifact.api import PluginMount, EDISyntaxError
from pydifact.segments import Segment as Seg, SegmentFactory


class BiDirectionalIterator(object):
    """
    Bi-directional iterator. Used as a convenience when parsing messages
    """

    def __init__(self, collection):
        self.collection = collection
        self.index = 0

    def next(self):
        try:
            result = self.collection[self.index]
            self.index += 1
        except IndexError:
            raise StopIteration
        return result

    def prev(self):
        self.index -= 1
        if self.index < 0:
            raise StopIteration
        return self.collection[self.index]

    def __iter__(self):
        return self


class AbstractMappingComponent:
    """
    Abstract EDIFact Component, used as a base for Segments, SegmentGroups,
    Loops
    """

    def __init__(self, **kwargs):
        self.mandatory = kwargs.get("mandatory", False)

    def _from_segments(self, messages):
        raise NotImplementedError()

    def _to_segments(self):
        raise NotImplementedError()


class Segment(AbstractMappingComponent):
    """
    EDIFact Component.
    A simple wrapper for Segment
    """

    def __init__(self, tag: str, *elements, **kwargs):
        super(Segment, self).__init__(**kwargs)

        self.__component__ = SegmentFactory.create_segment(tag, [], validate=False)

    @property
    def tag(self):
        return self.__component__.tag

    def __str__(self):
        return "{} {}".format(type(self.__component__), str(self.__component__))

    def __getitem__(self, key):
        return self.__component__[key]

    def __setitem__(self, key, value):
        self.__component__[key] = value

    def validate(self) -> bool:
        return self.__component__.validate()

    def _from_segments(self, iterator):
        segment = iterator.next()

        if self.tag == segment.tag:
            self.__component__ = segment
            return

        if self.mandatory:
            raise EDISyntaxError("Missing %s, found %s" % (self.tag, segment))

        iterator.prev()

    def _to_segments(self):
        return self.__component__


class SegmentGroupMetaClass(type):
    """
    Metaclass to maintain an ordered list of components.
    Required for compatibility with Python 3.5. In 3.6 the
    properties of a class are strictly ordered.
    """

    @classmethod
    def __prepare__(cls, name, bases):
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

    def _from_segments(self, isegment):
        i = 0

        icomponent = iter(self.__components__)

        try:
            while True:
                component_name = next(icomponent)
                component = getattr(self, component_name)
                component._from_segments(isegment)
        except StopIteration:
            pass

    def _to_segments(self):
        segments = []

        for component_name in self.__components__:
            component = getattr(self, component_name)
            component_segments = component._to_segments()

            if isinstance(component_segments, list):
                segments += component_segments
            else:
                segments.append(component_segments)

        return segments

    def from_message(self, message):
        imessage = BiDirectionalIterator(message.segments)
        self._from_segments(imessage)

    def to_message(self, reference_number: str, identifier: Tuple):
        segments = self._to_segments()
        return Message.from_segments(reference_number, identifier, segments)

    def __str__(self):
        res = []
        for component_name in iter(self.__components__):
            component = getattr(self, component_name)
            res.append(str(component))
        return "\n".join(res)


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

    def _from_segments(self, isegment):
        i = 0
        while i < self.max:

            try:
                component = self.__component__()
                component._from_segments(isegment)
                self.value.append(component)
            except EDISyntaxError:
                isegment.prev()
                if self.mandatory and i < self.min:
                    raise EDISyntaxError("Missing %s" % (self.__component__.__name__))
                break

            i += 1

        if i < self.min:
            raise EDISyntaxError("Minimum required not met")

    def _to_segments(self):
        segments = []

        for value in self.value:
            segments += value._to_segments()

        return segments

    def __str__(self):
        res = []
        for v in self.value:
            res.append(str(v))
        return "{} = {}".format(self.__component__.__name__, str(res))

    def __getitem__(self, key):
        return self.value[key]

    def __setitem__(self, key, value):
        self.value[key] = value
