"""Meaningful structural negative controls for macro recovery.

Copies current state in memory only. Never edits evidence, advances cadence,
queries runtime, or certifies a mathematical claim.
"""
import copy
from research_state import ROOT, read_state, validate


def main():
    state, cadence = read_state()
    assert state['macro_control']['schema'] == 'macro-recovery-v2'
    failures = []

    def reject(name, change):
        s, c = copy.deepcopy(state), copy.deepcopy(cadence)
        change(s, c)
        try:
            validate(ROOT, s, c)
        except (KeyError, ValueError):
            failures.append(name)
        else:
            raise AssertionError('Unsafe recovery accepted: ' + name)

    def stale_audit(s, c):
        s['completion_audit'].update(goal='goals/GOAL.20261013.md',
                                     baseline_commit=s['historical_baseline_commit'],
                                     mathematical_gate='passed')

    reject('old completion cannot bind new Goal', stale_audit)
    reject('wrong current Goal fingerprint',
           lambda s, c: s['macro_control'].update(goal_lf_sha256='0'*64))
    reject('duplicate completed iteration',
           lambda s, c: c['last_completed_round_note_paths'].append(c['last_completed_round']))
    reject('unpaid contract settlement',
           lambda s, c: s['primary_contract'].update(settled_iterations=['notes/not-settled.md']))
    reject('contract admission silently reset/exceeded',
           lambda s, c: s['primary_contract'].update(
               settled_iterations=c['last_completed_round_note_paths'][:3], iteration_budget=2))
    reject('lost process handle/observation',
           lambda s, c: s.update(pending_processes=[{'status':'unknown'}]))
    reject('pending output escapes repository',
           lambda s, c: s.update(pending_processes=[{
               'handle_type':'exec-session','handle':'memory-only-test','status':'unknown',
               'observed_at':'test','next_action':'inspect existing output',
               'output_paths':['../outside-workspace.txt']}]))
    # Honest uncertainty is admissible; deleting unknowns is not a prerequisite.
    s = copy.deepcopy(state)
    s['pending_processes'] = [{'handle_type':'exec-session','handle':'memory-only-test',
                              'status':'unknown','observed_at':'test',
                              'next_action':'inspect original session before rerunning',
                              'output_paths':['tmp/future-output.json']}]
    validate(ROOT, s, cadence)
    print('Seven unsafe-state controls rejected; honest unknown process preserved.')
    print('Scope: structure only; no mathematical certification or cadence mutation.')


if __name__ == '__main__':
    main()
