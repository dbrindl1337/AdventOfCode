from ..solution import part_a as a
from ..solution import part_b as b

input_a = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""


def test_correct_example_solution_part_a():
    assert a.return_solution(input_a) == 150


def test_correct_example_solution_part_b():
    assert b.return_solution(input_a) == 900
