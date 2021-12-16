from ..solution import part_a as a
from ..solution import part_b as b

input_a = """D2FE28"""
input_a_1 = """38006F45291200"""
input_a_2 = """EE00D40C823060"""
input_a_3 = """8A004A801A8002F478"""
input_a_4 = """620080001611562C8802118E34"""
input_a_5 = """C0015000016115A2E0802F182340"""
input_a_6 = """A0016C880162017C3686B18A3D4780"""

input_b = input_a  # replace me


def test_correct_example_solution_part_a():
    assert a.return_solution(a.split_input(input_a)) == 6


def test_correct_example_solution_part_a_1():
    assert a.return_solution(a.split_input(input_a)) == 9


def test_correct_example_solution_part_a_2():
    assert a.return_solution(a.split_input(input_a)) == 19


def test_correct_example_solution_part_a_3():
    assert a.return_solution(a.split_input(input_a)) == 16


def test_correct_example_solution_part_a_4():
    assert a.return_solution(a.split_input(input_a)) == 23


def test_correct_example_solution_part_a_5():
    assert a.return_solution(a.split_input(input_a)) == 31


def test_correct_example_solution_part_a_6():
    assert a.return_solution(a.split_input(input_a)) == 6


def test_correct_example_solution_part_b():
    assert b.return_solution(b.split_input(input_b)) == 0  # replace me
