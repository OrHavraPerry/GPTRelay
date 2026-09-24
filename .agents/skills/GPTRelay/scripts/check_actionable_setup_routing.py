"""Illustrative contract checks for local setup routing, not a skill behavior test."""

from dataclasses import dataclass


@dataclass(frozen=True)
class State:
    work_kind: str
    bounded_known: bool = False
    trivial_check: bool = False
    transfer_cost_exceeds_benefit: bool = False


ACTIONABLE_KINDS = {"setup", "launch", "playtest-prep", "test-execution"}


def route(state: State) -> str:
    if state.work_kind not in ACTIONABLE_KINDS or state.trivial_check:
        return "parent_only_allowed"
    if state.transfer_cost_exceeds_benefit:
        return "parent_may_execute_with_reason"
    if state.bounded_known:
        return "in_process_luna_high"
    return "in_process_sol_medium"


CASES = {
    "known launch uses Luna": (
        State(work_kind="launch", bounded_known=True), "in_process_luna_high"
    ),
    "known playtest prep uses Luna": (
        State(work_kind="playtest-prep", bounded_known=True), "in_process_luna_high"
    ),
    "uncertain dependency setup uses Sol": (
        State(work_kind="setup"), "in_process_sol_medium"
    ),
    "uncertain test execution uses Sol": (
        State(work_kind="test-execution"), "in_process_sol_medium"
    ),
    "sequential substantive work still uses worker": (
        State(work_kind="setup", bounded_known=True), "in_process_luna_high"
    ),
    "explicit transfer-cost exception stays local": (
        State(work_kind="launch", transfer_cost_exceeds_benefit=True),
        "parent_may_execute_with_reason",
    ),
    "trivial status check remains parent-only": (
        State(work_kind="launch", trivial_check=True), "parent_only_allowed"
    ),
}


for name, (state, expected) in CASES.items():
    actual = route(state)
    assert actual == expected, f"{name}: {actual!r} != {expected!r}"
    print(f"PASS: {name}")
