"""Run all reproducible finite sanity checks.

These checks validate implementation identities only. They are not interval
certificates and are not evidence for RH.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


SCRIPTS = Path(__file__).resolve().parent
CHECKS = (
    (
        "Mellin dual separator",
        [sys.executable, "test_mellin_dual_separator.py"],
    ),
    ("prolate boundary correction", [sys.executable, "test_prolate_candidate.py"]),
    ("QW formulas and tails", [sys.executable, "test_qw_bounds.py"]),
    (
        "frozen Vaughan/Laurent channels",
        [sys.executable, "audit_vaughan_laurent_channels.py", "--frozen-test"],
    ),
)


def main() -> None:
    for label, command in CHECKS:
        print(f"==> {label}", flush=True)
        subprocess.run(command, cwd=SCRIPTS, check=True)
    print("All finite sanity checks passed.")


if __name__ == "__main__":
    main()