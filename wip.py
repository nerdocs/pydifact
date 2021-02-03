from pydifact.segmentcollection import Interchange
from pydifact.segments import Segment
import pydifact.mapping as mapping


class BGM(Segment):
    __omitted__ = False

    tag = "BGM"


class LIN(Segment):
    __omitted__ = False

    tag = "LIN"


interchange = Interchange.from_str(
    """UNA:+.?*'
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
UNZ+1+0001'"""
)


class OrderLine(mapping.SegmentGroup):
    line_id = mapping.Segment("LIN", mandatory=True)
    description = mapping.Segment("IMD", mandatory=True)
    quantity = mapping.Segment("QTY", mandatory=True)
    moa = mapping.Segment("MOA")
    pri = mapping.Segment("PRI")
    rff = mapping.Segment("RFF", mandatory=True)


class Order(mapping.SegmentGroup):
    purchase_order_id = mapping.Segment("BGM", mandatory=True)
    date = mapping.Segment("DTM", mandatory=True)
    delivery_date = mapping.Segment("DTM", mandatory=True)
    delivery_instructions = mapping.Segment("FTX", mandatory=True)
    supplier_id_gln = mapping.Segment("NAD", mandatory=True)
    supplier_id_tprg = mapping.Segment("NAD", mandatory=True)
    ref = mapping.Segment("RFF", mandatory=True)
    ship_to = mapping.Segment("NAD", mandatory=True)

    ship_to_contact = mapping.Segment("CTA", mandatory=True)
    ship_to_phone = mapping.Segment("COM", mandatory=True)
    ship_to_email = mapping.Segment("COM", mandatory=True)
    cux = mapping.Segment("CUX", mandatory=True)
    tdt = mapping.Segment("TDT", mandatory=True)

    lines = mapping.Loop(OrderLine, max=99, mandatory=True)

    uns = mapping.Segment("UNS", mandatory=True)
    cnt = mapping.Segment("CNT", mandatory=True)


TYPE_TO_PARSER_DICT = {"ORDERS": Order}

for message in interchange.get_messages():
    cls = TYPE_TO_PARSER_DICT.get(message.type)
    if not cls:
        raise NotImplementedError("Unsupported message type '{}'".format(message.type))

    obj = cls()
    obj.from_message(message)

    reconstituted = obj.to_message(message.reference_number, message.identifier)

    # print(str(obj))
    # print(obj.purchase_order_id[0])

    assert isinstance(obj.purchase_order_id._to_segments(), BGM)

    # print(message.segments)

    assert str(message) == str(
        reconstituted
    ), "Original message should match reconstituted message"
