import pytest

from gripper import GRIPPER_TIMEOUT_MS, grip_ok


def test_normal_grip_is_ok():
    assert grip_ok(300)


def test_grip_at_timeout_is_ok():
    assert grip_ok(GRIPPER_TIMEOUT_MS)


def test_slow_grip_is_rejected():
    assert not grip_ok(GRIPPER_TIMEOUT_MS + 1)


@pytest.mark.endurance
def test_endurance_10000_grips():
    failures = sum(not grip_ok(300) for _ in range(10_000))
    assert failures == 0
