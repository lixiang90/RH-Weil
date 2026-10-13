"""Validate and display the short research state; save recoverable checkpoints.

These are structural checks, not theorem verification or a runtime Goal API.
STATE is editable; cadence is referenced, never copied or advanced by this script.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import os
import re
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
STATE_PATH = Path("goals/STATE.json")
KINDS = {"proved", "conditional", "cited", "experiment", "obstruction", "open"}


def canonical(data):
    return (json.dumps(data, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


def resolve_file(root, relative):
    value = Path(relative.split("#", 1)[0])
    path = (root / value).resolve()
    if value.is_absolute() or not path.is_relative_to(root.resolve()):
        raise ValueError(f"Reference leaves repository: {relative}")
    if not path.is_file():
        raise ValueError(f"Missing referenced file: {relative}")
    return path


def validate(root, state, cadence):
    if state.get("schema") != "rh-weil-macro-state-v1":
        raise ValueError("Unknown state schema")
    if len(canonical(state)) > 16000:
        raise ValueError("STATE exceeds 16KB; remove historical detail")
    if any(k in state for k in ("rounds_since_review", "last_completed_round")):
        raise ValueError("Read round state from cadence; do not duplicate it")
    for key in ("goal", "workflow", "cadence", "decisions", "latest_strategy"):
        resolve_file(root, state[key])
    if state.get("latest_macro_review"):
        resolve_file(root, state["latest_macro_review"])
    decision_text = resolve_file(root, state["decisions"]).read_text(encoding="utf-8")
    decision_id = state.get("latest_decision", "")
    if not decision_id or not re.search(
            r"^## " + re.escape(decision_id) + r"(?:\b|[:：\s])",
            decision_text, re.MULTILINE):
        raise ValueError("Latest decision ID is absent from the decision file")
    if state["latest_strategy"] != cadence["latest_user_directed_review"]:
        raise ValueError("Strategy is stale relative to latest user-directed review")
    count = cadence["rounds_since_review"]
    if not isinstance(count, int) or not 0 <= count <= cadence["maximum_rounds"]:
        raise ValueError("Invalid review cadence")
    contract = state["primary_contract"]
    if not contract["id"] or not contract["next_action"].strip():
        raise ValueError("Primary contract needs identity and exact next action")
    if contract["status"] not in {"ready", "running", "reviewing", "completed", "stopped"}:
        raise ValueError("Unknown primary contract status")
    resolve_file(root, contract["path"])
    if len(state.get("support_contracts", [])) > 2:
        raise ValueError("More than two active support contracts")
    for item in state.get("support_contracts", []):
        resolve_file(root, item["path"])
    if not state["macro"]["unpaid_bottleneck"].strip() or not state["must_not_forget"]:
        raise ValueError("Macro bottleneck and retained constraints are required")
    for item in state["evidence"]:
        if item["kind"] not in KINDS or not item["scope"].strip():
            raise ValueError("Evidence needs a known kind and explicit scope")
        resolve_file(root, item["path"])
    if state.get("goal_completion_requested", False):
        raise ValueError("Completion is reviewed through the Goal tool, not a state flag")
    return True


def read_state(root=ROOT):
    state = json.loads((root / STATE_PATH).read_text(encoding="utf-8"))
    cadence = json.loads(resolve_file(root, state["cadence"]).read_text(encoding="utf-8"))
    validate(root, state, cadence)
    return state, cadence


def atomic_write(path, raw):
    path.parent.mkdir(parents=True, exist_ok=True)
    handle, name = tempfile.mkstemp(prefix=path.name + ".", dir=path.parent)
    try:
        with os.fdopen(handle, "wb") as stream:
            stream.write(raw)
        os.replace(name, path)
    finally:
        if os.path.exists(name):
            os.unlink(name)


def checkpoint(root, state, cadence, output):
    destination = (root / output).resolve()
    base = (root / "goals/checkpoints").resolve()
    if not destination.is_relative_to(base) or destination == base:
        raise ValueError("Checkpoint must be a file inside goals/checkpoints")
    if destination.exists():
        raise ValueError("Checkpoint exists; use a new filename to retain history")
    updated = copy.deepcopy(state)
    updated["checkpoint"] = destination.relative_to(root).as_posix()
    paths = {STATE_PATH.as_posix(), "AGENTS.md", "scripts/research_state.py",
             state["goal"], state["workflow"], state["cadence"], state["decisions"],
             state["latest_strategy"], state["primary_contract"]["path"]}
    paths |= {item["path"] for item in state["evidence"]}
    paths |= {item["path"] for item in state.get("support_contracts", [])}
    if state.get("latest_macro_review"):
        paths.add(state["latest_macro_review"])
    hashes = {}
    for relative in sorted(paths):
        raw = canonical(updated) if relative == STATE_PATH.as_posix() else resolve_file(root, relative).read_bytes()
        hashes[relative] = hashlib.sha256(raw.replace(b"\r\n", b"\n")).hexdigest()
    record = {
        "schema": "rh-weil-macro-checkpoint-v1",
        "created_for_client_date": updated["updated_for_client_date"],
        "git_head_at_checkpoint": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=root).decode().strip(),
        "state": updated, "cadence_snapshot": cadence, "normalized_lf_sha256": hashes,
        "scope": "Structural recovery snapshot; not proof or live runtime verification",
    }
    # The snapshot is written first; an interruption cannot point STATE at a missing file.
    atomic_write(destination, canonical(record))
    atomic_write(root / STATE_PATH, canonical(updated))
    return destination


def check_checkpoint(root, state):
    relative = state.get("checkpoint")
    if not relative:
        raise ValueError("No checkpoint registered")
    record = json.loads(resolve_file(root, relative).read_text(encoding="utf-8"))
    for name, expected in record["normalized_lf_sha256"].items():
        raw = resolve_file(root, name).read_bytes().replace(b"\r\n", b"\n")
        if hashlib.sha256(raw).hexdigest() != expected:
            raise ValueError(f"Changed since checkpoint (inspect before reuse): {name}")
    return True


def show(state, cadence):
    print("Goal:", state["goal"])
    print("Baseline:", state["baseline_commit"])
    if state.get("latest_macro_review"):
        print("Latest macro review:", state["latest_macro_review"])
    print("Unpaid bottleneck:", state["macro"]["unpaid_bottleneck"])
    print("Why this contract:", state["macro"]["why_this_contract"])
    print("Primary:", state["primary_contract"]["id"], state["primary_contract"]["status"])
    print("Next action:", state["primary_contract"]["next_action"])
    print("Cadence:", cadence["rounds_since_review"], "/", cadence["maximum_rounds"],
          "; last complete:", cadence["last_completed_round"])
    print("Paused routes:", ", ".join(state["macro"]["paused_routes"]))
    print("Last runtime observation (not live):", state["runtime_goal_observation"])
    print("Pending processes:", state["pending_processes"])
    print("Constraints:")
    for item in state["must_not_forget"]:
        print(" -", item)
    print("Checkpoint:", state.get("checkpoint"))


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("show")
    check = sub.add_parser("check")
    check.add_argument("--checkpoint", action="store_true")
    save = sub.add_parser("checkpoint")
    save.add_argument("--output", required=True)
    args = parser.parse_args()
    try:
        state, cadence = read_state()
        if args.command == "show":
            show(state, cadence)
        elif args.command == "check":
            if args.checkpoint:
                check_checkpoint(ROOT, state)
            print("Research state verified structurally; no mathematical certification.")
        else:
            print(checkpoint(ROOT, state, cadence, args.output))
    except (KeyError, ValueError, OSError, json.JSONDecodeError) as exc:
        parser.exit(1, f"State check failed: {exc}\n")


if __name__ == "__main__":
    main()
