from ..solution import part_a as a
from ..solution import part_b as b

input = """1721
979
366
299
675
1456"""


def test_correct_example_solution_part_a():
    assert a.return_solution(input) == 514579


def test_correct_example_solution_part_b():
    assert b.return_solution(input) == 241861950
