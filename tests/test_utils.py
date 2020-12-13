from define.utils import kw, mw, distinguishing


def test_kw():
    assert kw((1, 2, 3), (1, 2, 3)) == 0
    assert kw((1, 2, 3), (3, 2, 1)) == 2
    assert kw((1, 1, 1), (2, 2, 2)) == 3


def test_mw():
    assert mw(0, (1, 1), [(1, 1), (1, 2), (2, 1), (2, 2)]) == 2
    assert mw(1, (1, 1), [(1, 1), (1, 2), (2, 1), (2, 2)]) == 2
    assert mw(0, (3, 3), [(1, 1), (1, 2), (2, 1), (2, 2)]) == 4
    assert mw(1, (3, 3), [(1, 1), (1, 2), (2, 1), (2, 2)]) == 4


def test_distinguishing():
    assert all([a == b for a, b in zip(distinguishing((1, 1, 1), (2, 2, 2)), [0, 1, 2])])
    assert all([a == b for a, b in zip(distinguishing((2, 1, 1), (2, 2, 2)), [1, 2])])
    assert all([a == b for a, b in zip(distinguishing((2, 2, 1), (2, 2, 2)), [2])])
    assert all([a == b for a, b in zip(distinguishing((2, 1, 2), (2, 2, 2)), [1])])
    assert all([a == b for a, b in zip(distinguishing((2, 2, 2), (2, 2, 2)), [])])
