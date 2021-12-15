from aocd.models import Puzzle
from aocd import submit

import numpy as np


def return_solution(puzzle):
    flashes_in_step = 0
    step_count = 0

    while True:
        puzzle += 1
        flashable = np.where(puzzle == 10)

        while len(flashable[0]) > 0:
            for i in range(0, len(flashable[0])):
                puzzle[(flashable[0][i] - 1):(flashable[0][i] + 2), (flashable[1][i] - 1):(flashable[1][i] + 2)] += 1
                puzzle[flashable[0][i], flashable[1][i]] = -2000000
                flashes_in_step += 1
            flashable = np.where(puzzle > 9)

        puzzle[puzzle < -1000000] = 0
        if flashes_in_step == 100:
            break
        flashes_in_step = 0
        step_count += 1

    return step_count + 1


def split_input(puzzle):
    lines = puzzle.split("\n")

    frame = np.zeros((len(lines) + 2, len(lines[0]) + 2), dtype=int) - 1000000
    frame[1:-1, 1:-1] = 1
    input_values = np.array([[int(char) for char in line] for line in lines])

    x = 1
    y = 1

    frame[x:x + input_values.shape[0], y:y + input_values.shape[1]] = input_values

    return frame


def main():
    puzzle = Puzzle(year=2021, day=11)
    submit(return_solution(split_input(puzzle.input_data)), part="b", day=11, year=2021)


if __name__ == '__main__':
    main()
