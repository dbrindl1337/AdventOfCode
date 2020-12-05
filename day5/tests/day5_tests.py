from ..solution import part_a as a
from aocd.models import Puzzle
from ..solution import part_b as b

first_seat = """BFFFBBFRRR"""
second_seat = """FFFBBBFRRR"""
third_seat = """BBFFBBFRLL"""

seat_list = """BFFFBBFRRR
FFFBBBFRRR
BBFFBBFRLL"""


def test_correct_example_solution_part_a():
    assert a.get_seat_id(first_seat[::-1]) == 567
    assert a.get_seat_id(second_seat[::-1]) == 119
    assert a.get_seat_id(third_seat[::-1]) == 820


def test_highest_seat_number_part_a():
    assert a.return_solution(seat_list) == 820


def test_get_my_seat():
    puzzle = Puzzle(year=2020, day=5)
    seats = puzzle.input_data.split("\n")
    seat_map = list(map(b.get_seat_id, [seat[::-1] for seat in seats]))

    solution = b.return_solution(puzzle.input_data)

    assert solution not in seat_map
    assert solution - 1 in seat_map
    assert solution + 1 in seat_map
