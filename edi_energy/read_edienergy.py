import sys
from pathlib import Path

sys.path.append(str(Path().cwd()))

from pydifact.segmentcollection import Interchange
from pydifact.segments import Segment

TEST_DATA = Path().cwd() / "tests" / "data"
SAMPLE_DATA = Path().cwd() / "edi_energy"


def read_file(message_file) -> Interchange:
    return Interchange.from_file(message_file)


def get_header(message):
    # make some checks
     return message.get_header_segment() 
    #  == Segment(
        # "UNB", ["IATB", "1"], "6XPPC", "LHPPC", ["940101", "0950"], "1"
    # )
    #
    # assert message.get_segment("IFT") == Segment("IFT", "3", "XYZCOMPANY AVAILABILITY")
    # assert message.get_segment("TVL") == Segment(
    #     "TVL", ["240493", "1000", "", "1220"], "FRA", "JFK", "DL", "400", "C"
    # )


def main():
    wiki_edi = read_file(TEST_DATA / "wikipedia.edi")
    quotes = read_file(SAMPLE_DATA / "quotes.txt")
    
    get_header(quotes)


if __name__ == "__main__":
    main()