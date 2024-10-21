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


path = os.path.dirname(os.path.realpath(__file__)) + "/data"


def test_sage_coala_file():
    """test parsing a file generated by SAGE COALA"""
    interchange = Interchange.from_file("{}/sage_coala.ped".format(path))
    assert interchange
    assert interchange.get_header_segment() == Segment(
        "UNB",
        ["UNOL", "3"],
        ["99999999800028", "5", "I"],
        ["9215001", "146"],
        ["240704", "1032"],
        "20241861032cor",
        "",
        "",
        "",
        "",
        "TDT-PED-IN-TD2401",
    )
    assert interchange.get_segment("RFF") == Segment(
        "RFF", ["AUM", "SAGE Experts Comptables"]
    )


if __name__ == "__main__":
    test_sage_coala_file()
