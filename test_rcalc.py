
from pytest import mark
import rcalc


@mark.add
def test_add():
    assert 5 == rcalc.add(2, 3)
    assert 0 == rcalc.add(5, -5)
    assert 7 == rcalc.add(5, 2)

@mark.sub
def test_sub():
    assert 1 == rcalc.sub(3, 2)
    assert 3 == rcalc.sub(8, 5)
    assert -1 == rcalc.sub(2, 3)

@mark.multi
def test_multi():
    assert 4 == rcalc.multi(2, 2)
    assert 10 == rcalc.multi(5, 2)
    assert 9 == rcalc.multi(3, 3)

@mark.div
def test_div():
    assert 2 == rcalc.div(10, 5)
    assert 0 == rcalc.div(0, 5)
    assert 3 == rcalc.div(9, 3)
