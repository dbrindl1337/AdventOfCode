from ..solution import part_a as a
from ..solution import part_b as b

input_a = """199
200
208
210
200
207
240
269
260
263"""


def test_correct_example_solution_part_a():
    assert a.return_solution(input_a) == 7


def test_correct_example_solution_part_b():
    assert b.return_solution(input_a) == 5
