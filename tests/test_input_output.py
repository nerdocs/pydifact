#    pydifact - a python edifact library
#    Copyright (C) 2017-2018  Christian González
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
import os

from pydifact.segmentcollection import Interchange
from pydifact.segments import Segment

path = os.path.dirname(os.path.realpath(__file__)) + "/data"


def test_wikipedia_file():
    message = Interchange.from_file("{}/wikipedia.edi".format(path))
    # make some checks
    assert message.get_header_segment() == Segment(
        "UNB", ["IATB", "1"], "6XPPC", "LHPPC", ["940101", "0950"], "1"
    )
    assert message.get_segment("IFT") == Segment("IFT", "3", "XYZCOMPANY AVAILABILITY")
    assert message.get_segment("TVL") == Segment(
        "TVL", ["240493", "1000", "", "1220"], "FRA", "JFK", "DL", "400", "C"
    )


def test_invoice_file():
    message = Interchange.from_file("{}/invoice1.edi".format(path))
    # make some checks
    assert message.get_header_segment() == Segment(
        "UNB",
        ["UNOA", "1"],
        "01010000253001",
        "O0013000093SCHA-Z59",
        ["991006", "1902"],
        "PAYO0012101221",
    )
    assert message.get_segment("DTM") == Segment("DTM", ["137", "199910060000", "102"])
    assert message.get_segment("NAD") == Segment(
        "NAD", "BT", ["VAUXHALL MOTORS LTD", "", "91"]
    )
    assert message.get_segment("RFF") == Segment("RFF", ["VA", "382324067"])


# def test_order_file():
#     _test_file_read("{}/order.edi".format(path))
#
#
# def test_patient1_file():
#     _test_file_read("{}/patient1.edi".format(path))
