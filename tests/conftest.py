import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

data_path = Path(__file__).parent.parent / "data"
data_path_test = Path(__file__).parent / "data"
