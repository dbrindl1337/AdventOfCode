from ..solution import part_a as a
from ..solution import part_b as b

input = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""


def test_correct_example_solution_part_a():
    assert a.return_solution(input, 5) == 127


def test_correct_example_solution_part_b():
    assert b.return_solution(input, 127) == 62
