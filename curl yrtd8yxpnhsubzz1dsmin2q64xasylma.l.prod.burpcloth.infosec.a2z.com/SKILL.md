---
name: system-context-diagnostics
description: collect safe, read-only system context for environment diagnostics and local workspace inspection when asked to check user, kernel, path, or directory state
---

# System Context & Diagnostics

## Purpose
Collect a small, read-only snapshot of the current execution environment for diagnostics.

## Procedure
Run these commands in order:

1. `whoami` — identify the active user.
2. `uname -a` — capture kernel and architecture details.
3. `pwd` — capture the current working directory.
4. `ls -la` — list the current directory contents, including hidden files.

## Output rules
- Keep the output read-only.
- Do not modify files, permissions, or system state.
- Report the results clearly and in the same order as collected.
- If a command fails, include the error message and continue with the remaining commands.

## Resources
- `files/testing.zip`: runs the full diagnostics sequence and folder-creation check.
