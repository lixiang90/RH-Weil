"""Fast coverage/dispatch checks for CI groups; never run a heavy certificate."""

from __future__ import annotations

from collections import Counter
from contextlib import redirect_stderr, redirect_stdout
from io import StringIO
from pathlib import Path
import sys
from unittest.mock import patch

import run_checks


def signatures(checks):
    return Counter((label, tuple(command)) for label, command in checks)


def expect_value_error(call):
    try:
        call()
    except ValueError:
        return
    raise AssertionError("invalid or incomplete grouping was accepted")


def main() -> None:
    registered = run_checks.CHECKS
    groups = {
        name: run_checks.checks_for_group(name)
        for name in ("core", "b1h", "b1i")
    }
    assert run_checks.checks_for_group() == registered
    assert run_checks.checks_for_group("all") == registered
    combined = tuple(check for group in groups.values() for check in group)
    assert signatures(combined) == signatures(registered)
    assert len(combined) == len(registered)
    for name, script in run_checks.HEAVY_CHECK_SCRIPTS.items():
        assert len(groups[name]) == 1
        assert Path(groups[name][0][1][1]).name == script
    expected_core = tuple(
        check for check in registered
        if Path(check[1][1]).name not in run_checks.HEAVY_CHECK_SCRIPTS.values()
    )
    assert groups["core"] == expected_core
    assert len(groups["core"]) == len(registered) - 2
    assert sum(
        Path(command[1]).name == "test_check_groups.py"
        for _, command in registered
    ) == 1

    future = ("future ordinary check", [sys.executable, "future_check.py", "--exact"])
    extended = registered + (future,)
    assert run_checks.checks_for_group("core", extended) == expected_core + (future,)
    assert run_checks.checks_for_group("b1h", extended) == groups["b1h"]
    assert run_checks.checks_for_group("b1i", extended) == groups["b1i"]
    assert signatures(
        check for name in groups
        for check in run_checks.checks_for_group(name, extended)
    ) == signatures(extended)

    expect_value_error(lambda: run_checks.checks_for_group("typo"))
    for name in ("b1h", "b1i"):
        missing = tuple(check for check in registered if check != groups[name][0])
        duplicate = registered + groups[name]
        expect_value_error(lambda: run_checks.checks_for_group(name, missing))
        expect_value_error(lambda: run_checks.checks_for_group(name, duplicate))

    # Mock subprocess for every dispatch test: no registered script is run.
    for argv, expected in (
        ([], registered),
        (["--group", "all"], registered),
        *((["--group", name], selected) for name, selected in groups.items()),
    ):
        with patch.object(run_checks.subprocess, "run") as execute, redirect_stdout(StringIO()):
            run_checks.main(argv)
        assert len(execute.call_args_list) == len(expected)
        for call, (_, command) in zip(execute.call_args_list, expected):
            assert call.args == (command,)
            assert call.kwargs == {"cwd": run_checks.SCRIPTS, "check": True}
    with patch.object(run_checks.subprocess, "run") as execute, redirect_stderr(StringIO()):
        try:
            run_checks.main(["--group", "typo"])
        except SystemExit as error:
            assert error.code == 2
        else:
            raise AssertionError("invalid CLI group did not fail")
        execute.assert_not_called()

    print(
        f"Check groups passed: core={len(groups['core'])}, b1h=1, b1i=1, "
        f"all={len(registered)}; no checks skipped or duplicated"
    )
    print("[scope] registry coverage and mocked dispatch only; no heavy computations")


if __name__ == "__main__":
    main()
