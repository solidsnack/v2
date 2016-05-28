from v2 import v2


def test_basics():
    # Doesn't crash.
    v2.from_file().from_pkg().from_git().from_default()
