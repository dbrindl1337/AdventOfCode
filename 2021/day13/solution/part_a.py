from aocd.models import Puzzle
from aocd import submit

import numpy as np


def return_solution(puzzle):
    dots = puzzle[0]
    folding = puzzle[1][0]
    axis = 0 if folding[0] == 'y' else 1
    folding_area_bottom = dots[:folding[1]] if axis == 0 else dots[:, :folding[1]]
    folding_area_top = dots[folding[1] + 1:] if axis == 0 else dots[:, folding[1] + 1:]

    return np.count_nonzero(folding_area_bottom | np.flip(folding_area_top, axis))


def split_input(puzzle):
    lines = puzzle.split("\n\n")

    dot_positions = np.array([list(map(lambda x: int(x), line.split(","))) for line in lines[0].split("\n")])
    max_x = max(dot_positions[:, 0]) + 1
    max_y = max(dot_positions[:, 1]) + 1

    dots = np.full((max_y, max_x), False)

    for dot in dot_positions:
        dots[dot[1], dot[0]] = True

    folding_instructions = list(
        map(lambda s: list(map(lambda x: int(x) if x.isdigit() else x, s[len("fold along "):].split("="))),
            lines[1].split("\n")))

    return dots, folding_instructions


def main():
    puzzle = Puzzle(year=2021, day=13)
    submit(return_solution(split_input(puzzle.input_data)), part="a", day=13, year=2021)


if __name__ == '__main__':
    main()
