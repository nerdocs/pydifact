from typing import Callable, List, Optional, Tuple, Union


from pydifact.segmentcollection import Interchange
from pydifact.segments import Segment, SegmentProvider



interchange = Interchange.from_str("""UNA:+.?*'
UNB+UNOA:4+5021376940009:14+1111111111111:14+200421:1000+0001+ORDERS'
UNH+1+ORDERS:D:01B:UN:EAN010'
BGM+220+123456+9'
DTM+137:20150410:102'
DTM+2:20150710:102'
FTX+DIN+++DELIVERY INSTRUCTIONS DESCRIPTION'
NAD+BY+5021376940009::9'
NAD+SU+1111111111111::9'
RFF+IA:123456'
NAD+ST+++Mr John Smith+The Bungalow:Hastings Road+Preston+:::Lancashire+SW1A 1AA'
CTA+LB+:Mr John Smith'
COM+01772 999999:TE'
COM+johnsmith@gmail.com:EM'
CUX+2:GBP:9'
TDT+20+++++SD'
LIN+1++121354654:BP'
IMD+F++:::TPRG item description'
QTY+21:2'
MOA+203:200.00'
PRI+AAA:100.00'
RFF+LI:1'
LIN+1++121354654:BP'
IMD+F++:::TPRG item description'
QTY+21:2'
MOA+203:200.00'
PRI+AAA:100.00'
RFF+LI:1'
UNS+S'
CNT+2:1'
UNT+32+1'
UNZ+1+0001'""")

import itertools
import collections


class BiDirectionalIterator(object):
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


class AbstractComponent:
    """Abstract EDIFact Component, used as a base for Components, SegmentGroup, SegmentLoop"""
    def __init__(self, **kwargs):
        self.mandatory = kwargs.get("mandatory", False)

    def _from_segment_iter(self, messages):
        raise NotImplementedError()


class Component(AbstractComponent, Segment):
    """
    EDIFact Component.
    A simple wrapper for Segment
    """
    def __init__(
        self,
        tag: str,
        *elements,
        **kwargs
    ):
        AbstractComponent.__init__(self, **kwargs)
        Segment.__init__(self, tag, *elements)

    def _from_segment_iter(self, iterator):
        segment = iterator.next()

        if self.tag == segment.tag:
            self.elements = segment.elements
            return

        if self.mandatory:
            raise Exception("Missing %s, found %s" % (self.tag, segment))

        iterator.prev()


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
            if k not in exclude and isinstance(v, AbstractComponent):
                result.__components__.append(k)
        return result


class SegmentGroup(AbstractComponent, metaclass=SegmentGroupMetaClass):
    """
    Describes a static group of Components
    """
    def _from_segment_iter(self, isegment):
        i = 0

        icomponent = iter(self.__components__)

        try:
            while True:
                component_name = next(icomponent)
                component = getattr(self, component_name)
                component._from_segment_iter(isegment)
        except StopIteration:
            pass

    def from_message(self, message):
        imessage = BiDirectionalIterator(message.segments)
        self._from_segment_iter(imessage)

    def to_message(self):
        raise NotImplementedError()

    def __str__(self):
        res = []
        for component_name in iter(self.__components__):
            component = getattr(self, component_name)
            res.append(str(component))
        return "\n".join(res)


class SegmentLoop(AbstractComponent):
    """
    Describes a repeating SegmentGroup
    """
    def __init__(self, component, **kwargs):
        super(SegmentLoop, self).__init__(**kwargs)
        self.min = kwargs.get("min", 0)
        self.max = kwargs.get("max", 0)

        if self.mandatory and self.min < 1:
            self.min = 1

        if self.max < self.min:
            self.max = self.min

        self.__component__ = component
        self.value = []

    def _from_segment_iter(self, isegment):
        i = 0
        while i < self.max:

            try:
                component = self.__component__()
                component._from_segment_iter(isegment)
                self.value.append(component)
            except BaseException:
                isegment.prev()
                if self.mandatory and i < self.min:
                    raise Exception("Missing %s" %
                                    (self.__component__.__name__))
                break

            i += 1

        if i < self.min:
            raise Exception("minimum required not met")

    def __str__(self):
        res = []
        for v in self.value:
            res.append(str(v))
        return "{} = {}".format(
            self.__component__.__name__,
            str(res)
        )


class OrderLine(SegmentGroup):
    line_id = Component("LIN", mandatory=True)
    description = Component("IMD", mandatory=True)
    quantity = Component("QTY", mandatory=True)
    moa = Component("MOA")
    pri = Component("PRI")
    rff = Component("RFF", mandatory=True)




class Order(SegmentGroup):
    purchase_order_id = Component("BGM", mandatory=True)
    date = Component("DTM", mandatory=True)
    delivery_date = Component("DTM", mandatory=True)
    delivery_instructions = Component("FTX", mandatory=True)
    supplier_id_gln = Component("NAD", mandatory=True)
    supplier_id_tprg = Component("NAD", mandatory=True)
    ref = Component("RFF", mandatory=True)
    ship_to = Component("NAD", mandatory=True)

    ship_to_contact = Component("CTA", mandatory=True)
    ship_to_phone = Component("COM", mandatory=True)
    ship_to_email = Component("COM", mandatory=True)
    cux = Component("CUX", mandatory=True)
    tdt = Component("TDT", mandatory=True)

    lines = SegmentLoop(
        OrderLine,
        max=99,
        mandatory=True
    )

    uns = Component("UNS", mandatory=True)
    cnt = Component("CNT", mandatory=True)


TYPE_TO_PARSER_DICT = {
    "ORDERS": Order
}


for message in interchange.get_messages():
    cls = TYPE_TO_PARSER_DICT.get(message.type)
    if not cls:
        raise NotImplementedError("Unsupported message type '{}'".format(message.type))

    obj = cls()
    obj.from_message(message)
    print(str(obj))
