from ..solution import part_a as a
from ..solution import part_b as b
from ..solution import golf as t

input_a = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""

input_b = input_a  # replace me


def test_correct_example_solution_part_a():
    assert a.return_solution(a.split_input(input_a)) == 198


def test_correct_example_solution_part_b():
    assert b.return_solution(b.split_input_into_numbers(input_b)) == 230  # replace me
