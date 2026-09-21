#!/usr/bin/env python3
"""Print the supported Python versions declared in pyproject.toml.

The single source of truth is the list of ``Programming Language :: Python :: 3.X``
trove classifiers. Used by ``make test-all`` and the CI test matrix.

Usage:
    python scripts/python_versions.py          -> "3.10 3.11 3.12"
    python scripts/python_versions.py --json   -> '["3.10", "3.11", "3.12"]'
"""

import json
import re
import sys
from pathlib import Path

PYPROJECT = Path(__file__).resolve().parent.parent / "pyproject.toml"
PATTERN = re.compile(r'"Programming Language :: Python :: (3\.\d+)"')

versions = PATTERN.findall(PYPROJECT.read_text(encoding="utf-8"))
if not versions:
    sys.exit("No 'Programming Language :: Python :: 3.X' classifiers in pyproject.toml")

if "--json" in sys.argv:
    print(json.dumps(versions))
else:
    print(" ".join(versions))
