from ..solution import part_a as a
from ..solution import part_b as b

input_a = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

input_b = input_a


def test_correct_example_solution_part_a():
    assert a.return_solution(a.split_input(input_a)) == 157


def test_correct_example_solution_part_b():
    assert b.return_solution(b.split_input(input_b)) == 70
