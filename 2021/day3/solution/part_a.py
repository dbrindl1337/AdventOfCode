from aocd.models import Puzzle
from aocd import submit


def return_solution(puzzle):
    cols = len(puzzle[0])
    rows = len(puzzle)
    gamma = 0b0

    for i in range(0, cols):
        gamma <<= 1
        if sum([row[i] for row in puzzle]) > rows // 2:
            gamma += 1

    return gamma * (~gamma & 2**cols - 1)


def split_input(puzzle):
    return [[int(k) for k in i] for i in puzzle.split("\n")]


def main():
    puzzle = Puzzle(year=2021, day=3)
    submit(return_solution(split_input(puzzle.input_data)), part="a", day=3, year=2021)


if __name__ == '__main__':
    main()
