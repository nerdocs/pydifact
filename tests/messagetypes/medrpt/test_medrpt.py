from pydifact.syntax import v1
from pydifact.segmentcollection import Interchange


def test_medrpt(path):
    message = Interchange.from_file(f"{path}/patient1.edi")
