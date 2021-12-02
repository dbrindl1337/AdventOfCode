from ..solution import part_a as a
from ..solution import part_b as b

small_input = """16
10
15
5
1
11
7
19
6
12
4"""

large_input = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""


def test_correct_example_solution_part_a_small():
    assert a.return_solution(small_input) == 35


def test_correct_example_solution_part_a_large():
    assert a.return_solution(large_input) == 220


def test_correct_example_solution_part_b_small():
    assert b.return_solution(small_input) == 8


def test_correct_example_solution_part_b_large():
    assert b.return_solution(large_input) == 19208
