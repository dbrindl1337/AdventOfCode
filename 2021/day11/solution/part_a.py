from aocd.models import Puzzle
from aocd import submit

import numpy as np


def return_solution(puzzle):
    puzzle += 1



    pass


def split_input(puzzle):
    n = np.array([[int(char) for char in line] for line in puzzle.split("\n")])
    return n


def main():
    puzzle = Puzzle(year=2021, day=11)
    submit(return_solution(split_input(puzzle.input_data)), part="a", day=11, year=2021)


if __name__ == '__main__':
    main()
