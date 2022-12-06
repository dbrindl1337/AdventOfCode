from ..solution import part_a as a
from ..solution import part_b as b

input_a1 = """mjqjpqmgbljsphdztnvjfqwrcgsmlb"""
input_a2 = """bvwbjplbgvbhsrlpgdmjqwftvncz"""
input_a3 = """nppdvjthqldpwncqszvftbrmjlhg"""
input_a4 = """nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"""
input_a5 = """zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"""

input_b = input_a1


def test_correct_example_solution_part_a1():
    assert a.return_solution(a.split_input(input_a1)) == 7


def test_correct_example_solution_part_a2():
    assert a.return_solution(a.split_input(input_a2)) == 5


def test_correct_example_solution_part_a3():
    assert a.return_solution(a.split_input(input_a3)) == 6


def test_correct_example_solution_part_a4():
    assert a.return_solution(a.split_input(input_a4)) == 10


def test_correct_example_solution_part_a5():
    assert a.return_solution(a.split_input(input_a5)) == 11


def test_correct_example_solution_part_b1():
    assert b.return_solution(b.split_input(input_a1)) == 19


def test_correct_example_solution_part_b2():
    assert b.return_solution(b.split_input(input_a2)) == 23


def test_correct_example_solution_part_b3():
    assert b.return_solution(b.split_input(input_a3)) == 23


def test_correct_example_solution_part_b4():
    assert b.return_solution(b.split_input(input_a4)) == 29


def test_correct_example_solution_part_b5():
    assert b.return_solution(b.split_input(input_a5)) == 26
