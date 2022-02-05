import logging
import pathlib
import sys
import tempfile

import pytest

from foodsale import pathfromglob

if not sys.platform.startswith("win"):
    pytest.skip("only windows", allow_module_level=True)


"""
or this:
*/Program*/Windows Kits/*/bin/*/*/SignTool.exe
"""


def windows_test1():
    base_dir = pathlib.Path(tempfile.gettempdir())
    y1 = base_dir / "Program Files\WiX Toolset 3.11\bin\heat.exe"
    y1.parent.mkdir(parents=True, exist_ok=True)
    y1.touch()
    glob = pathfromglob.abspathglob(str(y1))
    result = list(glob)
    assert len(result) == 1
