#!/usr/bin/env python3
from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

FOLDER_NAME = "This Is Just a Folder"


def run_command(title: str, command: list[str]) -> int:
    print(f"\n## {title}")
    print(f"$ {' '.join(command)}")
    completed = subprocess.run(command, text=True, capture_output=True)
    if completed.stdout:
        print(completed.stdout, end="" if completed.stdout.endswith("\n") else "\n")
    if completed.stderr:
        print(completed.stderr, end="" if completed.stderr.endswith("\n") else "\n", file=sys.stderr)
    if completed.returncode != 0:
        print(f"[exit code: {completed.returncode}]", file=sys.stderr)
    return completed.returncode


def main() -> int:
    base_dir = Path.cwd()
    target_dir = base_dir / FOLDER_NAME
