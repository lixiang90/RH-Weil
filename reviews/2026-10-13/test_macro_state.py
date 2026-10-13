"""Recovery guard regressions; no mathematical assertions."""
import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location("research_state", ROOT / "scripts/research_state.py")
guard = importlib.util.module_from_spec(spec)
spec.loader.exec_module(guard)


class RecoveryTests(unittest.TestCase):
    def setUp(self):
        self.state, self.cadence = guard.read_state(ROOT)

    def rejected(self, state):
        with self.assertRaises(ValueError):
            guard.validate(ROOT, state, self.cadence)

    def test_current_recovery_is_valid(self):
        self.assertTrue(guard.validate(ROOT, self.state, self.cadence))

    def test_parent_path_cannot_become_current_goal(self):
        self.state["goal"] = "../GOAL.20260909.md"
        self.rejected(self.state)

    def test_copied_counter_is_rejected(self):
        self.state["rounds_since_review"] = 0
        self.rejected(self.state)

    def test_stale_strategy_is_rejected(self):
        self.state["latest_strategy"] = self.state["goal"]
        self.rejected(self.state)

    def test_nonexistent_latest_decision_is_rejected(self):
        self.state["latest_decision"] = "MISSING-DECISION"
        self.rejected(self.state)

    def test_unknown_evidence_cannot_be_promoted(self):
        self.state["evidence"][0]["kind"] = "certified_breakthrough"
        self.rejected(self.state)

    def test_missing_evidence_is_rejected(self):
        self.state["evidence"][0]["path"] = "notes/missing-recovery-evidence.md"
        self.rejected(self.state)

    def test_completion_cannot_be_set_by_state_flag(self):
        self.state["goal_completion_requested"] = True
        self.rejected(self.state)

    def test_resume_needs_exact_next_action(self):
        self.state["primary_contract"]["next_action"] = ""
        self.rejected(self.state)

    def test_parallel_queue_does_not_expand_without_bound(self):
        self.state["support_contracts"] = [{"path": self.state["primary_contract"]["path"]}] * 3
        self.rejected(self.state)

    def test_snapshot_survives_reload_and_detects_changed_goal(self):
        parent = ROOT / "tmp/macro-goal-20261013/state-tests"
        parent.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(dir=parent) as folder:
            fixture = Path(folder).resolve()
            self.assertTrue(fixture.is_relative_to(parent.resolve()))
            state = copy.deepcopy(self.state)
            files = {state[k] for k in ("goal", "workflow", "cadence", "decisions", "latest_strategy")}
            files |= {state["primary_contract"]["path"], "AGENTS.md", "scripts/research_state.py"}
            for name in files:
                target = fixture / name
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text("fixture", encoding="utf-8")
            (fixture / state["decisions"]).write_text(
                "## " + state["latest_decision"] + ": fixture\n", encoding="utf-8")
            for item in state["evidence"]:
                target = fixture / item["path"]
                target.parent.mkdir(parents=True, exist_ok=True)
                if not target.exists():
                    target.write_text("evidence fixture", encoding="utf-8")
            cadence_path = fixture / state["cadence"]
            cadence_path.write_bytes(guard.canonical(self.cadence))
            before = cadence_path.read_bytes()
            state_path = fixture / guard.STATE_PATH
            state_path.write_bytes(guard.canonical(state))
            with patch.object(guard.subprocess, "check_output", return_value=b"fixture-baseline\n"):
                guard.checkpoint(fixture, state, self.cadence, "goals/checkpoints/test.json")
            loaded = json.loads(state_path.read_text(encoding="utf-8"))
            self.assertTrue(guard.check_checkpoint(fixture, loaded))
            self.assertEqual(cadence_path.read_bytes(), before)
            evidence_path = fixture / state["evidence"][-1]["path"]
            saved_evidence = evidence_path.read_bytes()
            evidence_path.write_text("changed evidence", encoding="utf-8")
            with self.assertRaises(ValueError):
                guard.check_checkpoint(fixture, loaded)
            evidence_path.write_bytes(saved_evidence)
            (fixture / state["goal"]).write_text("changed target", encoding="utf-8")
            with self.assertRaises(ValueError):
                guard.check_checkpoint(fixture, loaded)
            with self.assertRaises(ValueError):
                guard.checkpoint(fixture, loaded, self.cadence, "goals/checkpoints/test.json")


if __name__ == "__main__":
    unittest.main()
