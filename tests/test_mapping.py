#    pydifact - a python edifact library
#    Copyright (C) 2021 Karl Southern
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
import unittest
from pydifact.segmentcollection import Interchange
from pydifact import Segment, mapping


class BGM(Segment):
    __omitted__ = False

    tag = "BGM"


class LIN(Segment):
    __omitted__ = False

    tag = "LIN"


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


SAMPLE = """UNA:+.?*'
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
LIN+1++1213546541:BP'
IMD+F++:::TPRG item description1'
QTY+21:21'
MOA+203:200.00'
PRI+AAA:100.00'
RFF+LI:1'
LIN+1++1213546542:BP'
IMD+F++:::TPRG item description2'
QTY+21:22'
MOA+203:200.00'
PRI+AAA:100.00'
RFF+LI:1'
UNS+S'
CNT+2:1'
UNT+1+27'
UNZ+1+0001'"""


class MappingTest(unittest.TestCase):

    def test_read_interchange(self):
        interchange = Interchange.from_str(SAMPLE)
        message = next(interchange.get_messages())

        try:
            obj = Order()
            obj.from_message(message)
        except Exception as err:
            raise AssertionError(
                "Could not read Message into Order mapping! {}".format(
                    repr(err)
                )
            )

    def test_ensure_mapped_bgm_segment(self):
        interchange = Interchange.from_str(SAMPLE)
        message = next(interchange.get_messages())

        obj = Order()
        obj.from_message(message)

        self.assertTrue(isinstance(obj.purchase_order_id.to_segments(), BGM))


if __name__ == "__main__":
    unittest.main()
