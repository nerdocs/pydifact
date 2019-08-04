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


# This is commented out, as it's only a performance benchmark, no real test.
# use this file with  python -m cProfile tests/test_huge_message
def performance_test_huge_message():
    """tests parsing a huge message"""
    message = Message.from_file("tests/data/huge_file2.edi")
    assert message


if __name__ == "__main__":
    # just call this function for profiling purposes
    test_huge_message()
