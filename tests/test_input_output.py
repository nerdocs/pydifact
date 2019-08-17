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
from pydifact.message import Message
import unittest
import os

from pydifact.segments import Segment

path = os.path.dirname(os.path.realpath(__file__)) + "/data"


def test_wikipedia_file():
    message = Message.from_file("{}/wikipedia.edi".format(path))
    # make some checks
    assert message.get_segment("UNB") == Segment(
        "UNB", ["IATB", "1"], "6XPPC", "LHPPC", ["940101", "0950"], "1"
    )
    assert message.get_segment("IFT") == Segment("IFT", "3", "XYZCOMPANY AVAILABILITY")
    assert message.get_segment("TVL") == Segment(
        "TVL", ["240493", "1000", "", "1220"], "FRA", "JFK", "DL", "400", "C"
    )


# def test_order_file():
#     _test_file_read("{}/order.edi".format(path))
#
#
# def test_patient1_file():
#     _test_file_read("{}/patient1.edi".format(path))
