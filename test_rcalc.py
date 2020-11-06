
from pytest import mark
import rcalc


@mark.add
def test_add(gen_operands):
    results = (4, 9, 5, 2)
    for result, operands in zip(results, gen_operands):
        assert result == rcalc.add(*(operands))

@mark.sub
def test_sub(gen_operands):
    results = (-2, 1, -1, 0)
    for result, operands in zip(results, gen_operands):
        assert result == rcalc.sub(*(operands))

@mark.multi
def test_multi(gen_operands):
    results = (3, 20, 6, 1)
    for result, operands in zip(results, gen_operands):
        assert result == rcalc.multi(*(operands))

@mark.div
def test_div(gen_operands):
    results = (0, 1, 0, 1)
    for result, operands in zip(results, gen_operands):
        assert result == rcalc.div(*(operands))
