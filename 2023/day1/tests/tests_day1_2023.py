from ..solution import part_a as a
from ..solution import part_b as b

input_a = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

input_b = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""


def test_correct_example_solution_part_a():
    assert a.return_solution(a.split_input(input_a)) == 142


def test_correct_example_solution_part_b():
    assert b.return_solution(b.split_input(input_b)) == 281
