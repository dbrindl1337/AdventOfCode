import numpy
from aocd.models import Puzzle
from aocd import submit
from scipy.ndimage import measurements
import numpy as np


def get_basins(input_field):
    input_field[input_field <= 9] = 1
    input_field[input_field > 9] = 0
    return input_field


def return_solution(input_field):
    basins = get_basins(input_field)
    lw, num = measurements.label(basins)
    areas = measurements.sum(basins, lw, index=np.arange(lw.max() + 1))
    return int(numpy.prod(areas[np.argpartition(areas, -3)[-3:]]))


def split_input(puzzle):
    lines = puzzle.split("\n")
    frame = 11 * np.ones((len(lines) + 2, len(lines[0]) + 2), dtype=int)
    frame[1:-1, 1:-1] = 1
    input_values = np.array([[int(char) + 1 for char in line] for line in lines])

    x = 1
    y = 1

    frame[x:x + input_values.shape[0], y:y + input_values.shape[1]] = input_values

    return frame


def main():
    puzzle = Puzzle(year=2021, day=9)
    submit(return_solution(split_input(puzzle.input_data)), part="b", day=9, year=2021)


if __name__ == '__main__':
    main()
