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


# This just tests that there's no EDISyntaxError
def test_message_with_colon_at_end():
    Interchange.from_file("tests/data/invoice_with_colon_at_end.edi")


def test_v3_messages():
    # list .edi files in tests/data/messages/v3 dir and create Interchanges from them
    for file in os.listdir("tests/data/messages/v3"):
        if file.endswith(".edi"):
            Interchange.from_file(f"tests/data/messages/v3/{file}")


def test_v4_messages():
    # list .edi files in tests/data/messages/v4 dir and create Interchanges from them
    for file in os.listdir("tests/data/messages/v4"):
        if file.endswith(".edi"):
            Interchange.from_file(f"tests/data/messages/v4/{file}")
