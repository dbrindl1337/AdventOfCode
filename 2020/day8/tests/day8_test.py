from ..solution import part_a as a
from ..solution import part_b as b

input = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""


def test_correct_example_solution_part_a():
    assert a.return_solution(input) == 5


def test_correct_example_solution_part_b():
    assert b.return_solution(input) == 8
