from ..solution import part_a as a
from ..solution import part_b as b

input_a = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""

input_b = input_a


def test_correct_example_solution_part_a():
    assert a.return_solution(a.split_input(input_a)) == 24000


def test_correct_example_solution_part_b():
    assert b.return_solution(b.split_input(input_b)) == 45000
