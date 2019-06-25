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

from pydifact.control.characters import Characters
import re


class Serializer:
    """Serialize a bunch of segments into an EDI message string."""

    def __init__(self, characters: Characters = None):
        super().__init__()
        if characters is None:
            characters = Characters()

        self.characters = characters

    def serialize(self, segments: list, with_una: bool = False) -> str:
        """Serialize all the passed segments.

        :param segments: A list of segments to serialize
        :param with_una: True if a UNA header should be written. Defauts to False.
        """

        message = ""

        if with_una:
            # create an EDIFACT header
            message = "UNA"
            message += self.characters.component_separator
            message += self.characters.data_separator
            message += self.characters.decimal_point
            message += self.characters.escape_character
            message += self.characters.reserved_character
            message += self.characters.segment_terminator

        # iter through all segments
        for segment in segments:
            # skip the UNA segment as we already have written it if requested
            if segment.tag == "UNA":
                continue
            message += segment.tag
            for element in segment.elements:
                message += self.characters.data_separator
                if type(element) == list:
                    for nr, subelement in enumerate(element):
                        element[nr] = self.escape(subelement)
                    message += self.characters.component_separator.join(element)
                else:
                    message += self.escape(element)

            message += self.characters.segment_terminator

        return message

    def escape(self, string: str or None) -> str:
        """Escapes control characters.

        :param string: The string to be escaped
        """

        if string is None:
            return ""
        assert type(string) == str

        characters = [
            self.characters.escape_character,
            self.characters.component_separator,
            self.characters.data_separator,
            self.characters.segment_terminator,
        ]
        replace_map = {}
        for character in characters:
            replace_map[character] = self.characters.escape_character + character

        # Thanks to "Bor González Usach" for this wonderful piece of code:
        # https://gist.github.com/bgusach/a967e0587d6e01e889fd1d776c5f3729
        substrs = sorted(replace_map, key=len, reverse=True)
        regexp = re.compile("|".join(map(re.escape, substrs)))

        return regexp.sub(lambda match: replace_map[match.group(0)], string)
