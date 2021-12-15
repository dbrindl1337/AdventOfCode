from ..solution import part_a as a
from ..solution import part_b as b

input_a_0 = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""

input_a_1 = """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc"""

input_a_2 = """fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW"""


def test_correct_example_solution_part_a_0():
    assert a.return_solution(a.split_input(input_a_0)) == 10


def test_correct_example_solution_part_a_1():
    assert a.return_solution(a.split_input(input_a_1)) == 19


def test_correct_example_solution_part_a_2():
    assert a.return_solution(a.split_input(input_a_2)) == 226


def test_correct_example_solution_part_b_0():
    assert b.return_solution(b.split_input(input_a_0)) == 36


def test_correct_example_solution_part_b_1():
    assert b.return_solution(b.split_input(input_a_1)) == 103


def test_correct_example_solution_part_b_2():
    assert b.return_solution(b.split_input(input_a_2)) == 3509
