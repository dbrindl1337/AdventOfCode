from ..solution import part_a as a
from ..solution import part_b as b

input_a = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""

input_b = input_a  # replace me


def test_correct_example_solution_part_a():
    assert a.return_solution(a.split_input(input_a), 10) == 1588


def test_correct_example_solution_part_b():
    assert b.return_solution(b.split_input(input_b), 40) == 2188189693529


def test_correct_example_solution_part_b_1():
    assert b.return_solution(b.split_input(input_b), 10) == 1588
