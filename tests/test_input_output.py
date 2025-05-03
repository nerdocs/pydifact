#    pydifact - a python edifact library
#    Copyright (C) 2017-2024  Christian González
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
from pydifact.syntax import v3

path = os.path.dirname(os.path.realpath(__file__)) + "/data"


def test_wikipedia_file_en():
    """This tests a file presented on the Wikipedia homepage "EDIFACT" -
    interestingly, it is not covered by EDIFACT standards, but uses a IATB syntax
    identifier string."""
    message = Interchange.from_file(f"{path}/wikipedia_en.edi")
    # make some checks
    assert message.get_header_segment() == Segment(
        "UNB", ["IATB", "1"], ["6XPPC", "ZZ"], ["LHPPC", "ZZ"], ["940101", "0950"], "1"
    )
    assert message.get_segment("IFT") == Segment("IFT", "3", "XYZCOMPANY AVAILABILITY")
    assert message.get_segment("TVL") == Segment(
        "TVL", ["240493", "1000", "", "1220"], "FRA", "JFK", "DL", "400", "C"
    )


def test_wikipedia_file_de():
    message = Interchange.from_file(f"{path}/wikipedia_de.edi")
    # make some checks
    assert message.get_header_segment() == v3.UNBSegment(
        ["UNOC", "3"],
        "Senderkennung",
        "Empfaengerkennung",
        ["060620", "0931"],
        "1",
        "",
        "1234567",
    )
    assert message.get_segment("BGM") == Segment("BGM", "220", "B10001")
    assert message.get_segment("QTY") == Segment("QTY", ["1", "1000"])
    assert message.get_segment("LIN") == Segment(
        "LIN", "1", "", ["Produkt Schrauben", "SA"]
    )


def test_invoice_file():
    message = Interchange.from_file(f"{path}/invoice1.edi")
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
#     _test_file_read(f"{path}/order.edi")
#
#
# def test_patient1_file():
#     _test_file_read(f"{path}/patient1.edi")
