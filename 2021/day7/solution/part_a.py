from aocd.models import Puzzle
from aocd import submit


def return_solution(puzzle):
    return min([sum([abs(k-i) for k in puzzle]) for i in range(0, len(puzzle))])


def split_input(puzzle):
    return [int(i) for i in puzzle.split(",")]


def main():
    puzzle = Puzzle(year=2021, day=7)
    submit(return_solution(split_input(puzzle.input_data)), part="a", day=7, year=2021)


if __name__ == '__main__':
    main()
