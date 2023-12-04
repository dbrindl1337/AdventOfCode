from ..solution import part_a as a
from ..solution import part_b as b

input_a = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

input_b = input_a  # replace me


def test_correct_example_solution_part_a():
    assert a.return_solution(a.split_input(input_a)) == 4361


def test_correct_example_solution_part_b():
    assert b.return_solution(b.split_input(input_b)) == 467835
