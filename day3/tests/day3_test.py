from ..solution import part_a as a
from ..solution import part_b as b

input = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""


def test_correct_example_solution_part_a_lambda():
    assert a.get_hits_functional(input) == 7


def test_correct_example_solution_part_a():
    assert a.get_hits(input) == 7


def test_correct_example_solution_part_b():
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    assert b.return_solution(input, slopes) == 336
