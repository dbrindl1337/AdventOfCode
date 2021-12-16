from ..solution import part_a as a
from ..solution import part_b as b

input_a = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""

input_b = input_a  # replace me


def test_correct_example_solution_part_a():
    assert a.return_solution(*a.split_input(input_a)) == 40  # replace me


def test_correct_example_solution_part_b():
    assert b.return_solution(*b.split_input(input_b)) == 315  # replace me
