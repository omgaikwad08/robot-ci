GRIPPER_TIMEOUT_MS = 300


def grip_ok(elapsed_ms):
    """A grasp is OK if it finished within the timeout."""
    return elapsed_ms <= GRIPPER_TIMEOUT_MS
