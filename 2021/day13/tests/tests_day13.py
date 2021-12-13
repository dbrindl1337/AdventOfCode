from ..solution import part_a as a
from ..solution import part_b as b

input_a = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""

input_b = input_a  # replace me


def test_correct_example_solution_part_a():
    assert a.return_solution(a.split_input(input_a)) == 17  # replace me


def test_correct_example_solution_part_b():
    assert b.return_solution(b.split_input(input_b)) == 16  # replace me
