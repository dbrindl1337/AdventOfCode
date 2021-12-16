from collections import defaultdict

from aocd.models import Puzzle
from aocd import submit


def calc_new_polymer(polymer, rules):
    pass


def return_solution(instructions, iteration_count):
    polymer = instructions[0]
    rules = instructions[1]


def split_input(puzzle):
    lines = puzzle.split("\n\n")

    template = lines[0]

    lines = dict([line.split(" -> ") for line in lines[1].split("\n")])
    return template, lines


def main():
    puzzle = Puzzle(year=2021, day=14)
    submit(return_solution(split_input(puzzle.input_data), 40), part="b", day=14, year=2021)


if __name__ == '__main__':
    main()
