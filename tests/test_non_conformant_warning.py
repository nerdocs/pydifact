import os
import warnings

import pytest

from pydifact.exceptions import NonConformantEDIWarning
from pydifact.parser import Parser
from pydifact.segmentcollection import Interchange

path = os.path.dirname(os.path.realpath(__file__)) + "/data"

UNB_V4 = "UNB+UNOA:4+SENDER+RECIPIENT+20240101:1200+REF1'UNZ+0+REF1'"
UNB_V3 = "UNB+UNOA:3+SENDER+RECIPIENT+240101:1200+REF1'UNZ+0+REF1'"


def test_content_before_una_warns():
    with pytest.warns(NonConformantEDIWarning, match="content before the UNA"):
        Interchange.from_file(f"{path}/sage_coala.ped")


def test_leading_whitespace_before_una_warns():
    with pytest.warns(NonConformantEDIWarning, match="Leading whitespace"):
        list(Parser().parse("\n UNA:+.? '" + UNB_V4))


def test_unb_date_not_matching_syntax_version_warns():
    with pytest.warns(NonConformantEDIWarning, match="does not match syntax version"):
        Interchange.from_str("UNB+UNOA:4+SENDER+RECIPIENT+240101:1200+REF1'UNZ+0+REF1'")
    with pytest.warns(NonConformantEDIWarning, match="does not match syntax version"):
        Interchange.from_str(
            "UNB+UNOA:3+SENDER+RECIPIENT+20240101:1200+REF1'UNZ+0+REF1'"
        )


@pytest.mark.parametrize("edi", [UNB_V4, UNB_V3, "UNA:+.? '" + UNB_V4])
def test_conformant_input_does_not_warn(edi):
    with warnings.catch_warnings():
        warnings.simplefilter("error", NonConformantEDIWarning)
        Interchange.from_str(edi)


def test_flag_suppresses_warnings():
    with warnings.catch_warnings():
        warnings.simplefilter("error", NonConformantEDIWarning)
        Interchange.from_file(f"{path}/sage_coala.ped", warn_non_conformant=False)
        Interchange.from_str(
            "\nUNA:+.? 'UNB+UNOA:4+SENDER+RECIPIENT+240101:1200+REF1'UNZ+0+REF1'",
            warn_non_conformant=False,
        )


def test_parser_flag_takes_precedence():
    """A given parser's setting applies, not the from_str() argument."""
    with warnings.catch_warnings():
        warnings.simplefilter("error", NonConformantEDIWarning)
        Interchange.from_file(
            f"{path}/sage_coala.ped", parser=Parser(warn_non_conformant=False)
        )
