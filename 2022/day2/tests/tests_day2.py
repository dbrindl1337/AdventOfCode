from ..solution import part_a as a
from ..solution import part_b as b

input_a = """A Y
B X
C Z"""

input_b = input_a


def test_correct_example_solution_part_a():
    assert a.return_solution(a.split_input(input_a)) == 15


def test_correct_example_solution_part_b():
    assert b.return_solution(b.split_input(input_b)) == 12
