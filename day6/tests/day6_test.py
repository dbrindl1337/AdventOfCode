from ..solution import part_a as a
from ..solution import part_b as b

input = """abc

a
b
c

ab
ac

a
a
a
a

b"""


def test_correct_example_solution_part_a():
    assert a.return_solution(input) == 11


def test_correct_example_solution_for_all_valid_part_b():
    assert b.return_solution(input) == 6
    pass
