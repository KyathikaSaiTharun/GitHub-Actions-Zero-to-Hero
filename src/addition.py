# app.py
# This is a test commit
# forked repo
def add(a, b):
    return a + b

def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0
    assert add(100,-120.1) == -20.1
