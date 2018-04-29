#    pydifact - a python edifact library
#    Copyright (C) 2017  Christian González
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

from pydifact.ControlCharacter import ControlCharacterMixin
import re


class Serializer(ControlCharacterMixin):
    """Serialize a bunch of segments into an EDI message string."""

    def __init__(self):
        super().__init__()

    def serialize(self, segments: list) -> str:
        """Serialize all the passed segments.

        :param segments: a list of segments to serialize
        """

        message = "UNA"
        message += self._component_separator
        message += self._data_separator
        message += self._decimal_point
        message += self._escape_character
        message += " "
        message += self._segment_terminator
        for segment in segments:
            message += segment.tag
            for element in segment.get_all_elements():
                message += self._data_separator
                if type(element) == list:
                    for nr, subelement in enumerate(element):
                        element[nr] = self.escape(subelement)
                    message += self._component_separator.join(element)
                else:
                    message += self.escape(element)

            message += self._segment_terminator

        return message

    def escape(self, string: str) -> str:
        """
        Escapes control characters.
        :param string the string to be escaped
        """

        assert(type(string) == str)

        characters = [
            self._escape_character,
            self._component_separator,
            self._data_separator,
            self._segment_terminator,
        ]
        replace_map = {}
        for character in characters:
            replace_map[character] = self._escape_character + character

        # Thanks to "Bor González Usach" for this wonderful piece of code:
        # https://gist.github.com/bgusach/a967e0587d6e01e889fd1d776c5f3729
        substrs = sorted(replace_map, key=len, reverse=True)
        regexp = re.compile('|'.join(map(re.escape, substrs)))

        return regexp.sub(lambda match: replace_map[match.group(0)], string)
