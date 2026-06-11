# System Context & Diagnostics Skill

## Overview
This skill allows the AI agent to securely audit its immediate execution environment. It captures structural operating system state, active path architecture, permissions context, and local storage layout by executing safe, immutable system calls.

## Monitored Parameters
When invoked, this tool sequentially collects and aggregates data from four isolated terminal primitives:
1. `whoami` — Assesses active user space context and security permissions.
2. `uname -a` — Profiles target host kernel release and core processor architecture.
3. `pwd` — Identifies absolute path location inside the system storage hierarchy.
4. `ls -la` — Maps current folder contents, target file sizes, ownership tags, and hidden objects.

---
