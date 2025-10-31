import os
import shutil
import subprocess
from pathlib import Path
import sys

import importlib.util
from pathlib import Path

# Add tools folder to sys.path for tests
tools_path = Path.cwd() / "tools"
import sys
sys.path.insert(0, str(tools_path))

from sync_to_comfy import sync_package


def test_sync_creates_target(tmp_path, monkeypatch):
    # Use tmpdir to simulate a ComfyUI custom_nodes folder
    dest = tmp_path / "custom_nodes"
    dest.mkdir()

    src = Path.cwd()
    target = sync_package(dest, src)

    assert target.exists()
    assert (target / "__init__.py").exists(), "package __init__.py should be copied"

    # cleanup
    shutil.rmtree(target)
