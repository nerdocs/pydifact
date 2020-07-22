# Pydifact - a python edifact library
#
# Copyright (c) 2019 Christian González
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from pydifact import segmentcollection, parser, segments, serializer, token, tokenizer

__version__ = "0.0.6"

from .control.characters import Characters
from .segmentcollection import SegmentCollection
from .parser import Parser
from .segments import Segment
from .serializer import Serializer
from .token import Token
from .tokenizer import Tokenizer

# generic EDIFACT implementation tutorial
# http://www.gxs.co.uk/wp-content/uploads/tutorial_edifact.pdf

# UNECE Syntax Implementation Guidelines
# https://www.unece.org/fileadmin/DAM/trade/untdid/texts/d423.htm

# UNECE Message Design Guidelines
# https://www.unece.org/fileadmin/DAM/trade/untdid/texts/d424_d.htm

# https://ecosio.com/de/blog/aufbau-einer-edifact-datei/ (German)
# https://www.stylusstudio.com/edifact/40102/codelist.htm
# https://www.hcs.at/wp-content/uploads/2012/12/hcs_AEK_Edifact_Text.pdf (German)
# https://www.hcs.at/wp-content/uploads/2012/12/hcs_AEK_Edifact_Labor.pdf (German)
