from aocd.models import Puzzle
from aocd import submit
import numpy as np


def return_solution(input_field):
    mask = ~((input_field < np.roll(input_field, 1, 0)) &
             (input_field < np.roll(input_field, -1, 0)) &
             (input_field < np.roll(input_field, 1, 1)) &
             (input_field < np.roll(input_field, -1, 1)))

    zeroes = np.zeros(shape=input_field.shape)

    solution = np.copy(input_field)
    solution[mask] = zeroes[mask]

    return sum(sum(solution))


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
    submit(return_solution(split_input(puzzle.input_data)), part="a", day=9, year=2021)


if __name__ == '__main__':
    main()
