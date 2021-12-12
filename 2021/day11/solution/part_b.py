from aocd.models import Puzzle
from aocd import submit


def return_solution(puzzle):
    pass


def split_input(puzzle):
    return puzzle.split("\n")


def main():
    puzzle = Puzzle(year=2021, day=11)
    submit(return_solution(split_input(puzzle.input_data)), part="b", day=11, year=2021)


if __name__ == '__main__':
    main()
