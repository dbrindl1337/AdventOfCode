from ..solution import part_a as a
from ..solution import part_b as b

input_a = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

input_b = input_a


def test_correct_example_solution_part_a():
    assert a.return_solution(a.split_input(input_a)) == "CMZ"


def test_correct_example_solution_part_b():
    assert b.return_solution(b.split_input(input_b)) == 'MCD'
