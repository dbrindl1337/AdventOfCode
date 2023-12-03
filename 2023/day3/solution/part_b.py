from aocd.models import Puzzle
from aocd import submit


def return_solution(lines):
    pass


def split_input(puzzle):
    lines = puzzle.split("\n")
    return lines


def main():
    puzzle = Puzzle(year=2023, day=3)
    submit(return_solution(split_input(puzzle.input_data)), part="b", day=3, year=2023)


if __name__ == '__main__':
    main()
