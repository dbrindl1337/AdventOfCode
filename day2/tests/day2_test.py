from ..aocd_solution import part_a as a
from ..aocd_solution import part_b as b

input = """1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc"""


def test_correct_example_solution_part_a():
    assert a.return_solution(input) == 2


def test_correct_example_solution_part_b():
    assert b.return_solution(input) == 1
