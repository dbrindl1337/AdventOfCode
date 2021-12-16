from aocd.models import Puzzle
from aocd import submit


def return_solution(lines):
    pass


def split_input(puzzle):
    lines = puzzle.split("\n")
    return lines


def main():
    puzzle = Puzzle(year=2021, day=16)
    submit(return_solution(split_input(puzzle.input_data)), part="b", day=16, year=2021)


if __name__ == '__main__':
    main()
