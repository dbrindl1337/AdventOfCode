from ..solution import part_a as a
from ..solution import part_b as b

input = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""


def test_correct_example_solution_part_a_small():
    assert a.return_solution(input) == 37


def test_correct_example_solution_part_b_small():
    assert b.return_solution(input) == 8
