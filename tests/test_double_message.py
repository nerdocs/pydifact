import pytest

from pydifact.exceptions import EDISyntaxError
from pydifact.segmentcollection import Interchange
from tests.test_input_output import path


def test_message_with_2_UNA_segments():
    with open(f"{path}/wikipedia_de.edi") as f:
        content = f.read()

    # doouble the message (2 UNA headers in one string!!)
    content = content + content

    with pytest.raises(EDISyntaxError):
        Interchange.from_str(content)
