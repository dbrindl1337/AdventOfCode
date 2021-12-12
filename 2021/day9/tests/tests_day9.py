from ..solution import part_a as a
from ..solution import part_b as b

input_a = """2199943210
3987894921
9856789892
8767896789
9899965678"""

input_b = input_a  # replace me


def test_correct_example_solution_part_a():
    assert a.return_solution(a.split_input(input_a)) == 15  # replace me


def test_correct_example_solution_part_b():
    assert b.return_solution(b.split_input(input_b)) == 1134  # replace me
