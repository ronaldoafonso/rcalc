
from pytest import fixture


@fixture
def gen_operands():
    return (1, 3), (5, 4), (2, 3), (1, 1)
