from ..solution import part_a as a
from ..solution import part_b as b

input_a = """3,4,3,1,2"""

input_b = input_a  # replace me


def test_correct_example_solution_part_a():
    assert a.return_solution(a.split_input(input_a), 18) == 26  # replace me
    assert a.return_solution(a.split_input(input_a), 80) == 5934  # replace me


def test_correct_example_solution_part_b():
    assert b.return_solution(b.split_input(input_b), 256) == 26984457539  # replace me
