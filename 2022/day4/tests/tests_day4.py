from ..solution import part_a as a
from ..solution import part_b as b

input_a = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""

input_b = input_a


def test_correct_example_solution_part_a():
    assert a.return_solution(a.split_input(input_a)) == 2


def test_correct_example_solution_part_b():
    assert b.return_solution(b.split_input(input_b)) == 4
