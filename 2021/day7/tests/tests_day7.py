from ..solution import part_a as a
from ..solution import part_b as b

input_a = """16,1,2,0,4,2,7,1,2,14"""

input_b = input_a  # replace me


def test_correct_example_solution_part_a():
    assert a.return_solution(a.split_input(input_a)) == 37  # replace me


def test_correct_example_solution_part_b():
    assert b.return_solution(b.split_input(input_b)) == 168  # replace me
