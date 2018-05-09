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


class InputOutputTest(unittest.TestCase):

    def setUp(self):
        self.path = os.path.dirname(os.path.realpath(__file__)) + "/data"

    def test1(self):
        self._test_file_read("{}/wikipedia.edi".format(self.path))

    def test2(self):
        self._test_file_read("{}/order.edi".format(self.path))

    def test_patient1(self):
        self.maxDiff = None
        self._test_file_read("{}/patient1.edi".format(self.path))

    def _test_file_read(self, file_name: str, encoding: str = 'iso8859-1'):

        # read in a complete message from a file
        message = Message.from_file(file_name)
        output = message.serialize()
        with open(file_name, encoding) as file:
            expected = file.read()  # .replace("\n", "")
            self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
