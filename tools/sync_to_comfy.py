#!/usr/bin/env python3
"""Sync the rathius-comfyui-nodes package into a ComfyUI `custom_nodes/` folder.

Usage:
    python tools/sync_to_comfy.py --dest C:/Projects/ComfyUI/custom_nodes

If no --dest is provided, the script will try to use the COMFYUI_PATH environment
variable or default to `C:/Projects/ComfyUI/custom_nodes` (useful for your current
workspace layout).

The script will copy the package folder contents into `<dest>/rathius_comfyui_nodes`.
It removes the destination folder first to ensure a clean replace.
"""

import argparse
import os
import shutil
import sys
from pathlib import Path


def sync_package(dest: Path, src: Path = None):
    if src is None:
        src = Path.cwd()
    dest = Path(dest)
    target = dest / "rathius_comfyui_nodes"

    if not src.exists():
        raise FileNotFoundError(f"Source folder {src} does not exist")

    # Ensure dest exists
    dest.mkdir(parents=True, exist_ok=True)

    # Remove target if exists
    if target.exists():
        shutil.rmtree(target)

    # Copy selectively to avoid copying venv or .git
    def ignore_func(directory, names):
        ignored = set()
        for n in names:
            if n in (".git", ".venv", "venv", "env", "__pycache__"):
                ignored.add(n)
            # skip node_modules, build artifacts
            if n in ("node_modules", "build", "dist"):
                ignored.add(n)
        return ignored

    shutil.copytree(src, target, ignore=ignore_func)
    return target


def main(argv=None):
    p = argparse.ArgumentParser()
    p.add_argument("--dest", help="ComfyUI custom_nodes folder path (default: env COMFYUI_PATH or C:\\Projects\\ComfyUI\\custom_nodes)")
    args = p.parse_args(argv)

    default = os.environ.get("COMFYUI_PATH")
    if args.dest:
        dest = Path(args.dest)
    elif default:
        dest = Path(default) / "custom_nodes"
    else:
        dest = Path("C:/Projects/ComfyUI/custom_nodes")

    src = Path.cwd()
    print(f"Syncing {src} -> {dest}")
    target = sync_package(dest, src)
    print(f"Copied to: {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
