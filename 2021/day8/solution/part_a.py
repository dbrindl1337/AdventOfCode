from aocd.models import Puzzle
from aocd import submit


def is_unique_len(digit):
    match len(digit):
        case 2:
            return True
        case 4:
            return True
        case 3:
            return True
        case 7:
            return True
        case _:
            return False


def return_solution(puzzle):
    return sum([sum([len(list(filter(is_unique_len, line.split())))]) for line in puzzle])


def split_input(puzzle):
    return [line.split(" | ")[1] for line in puzzle.split("\n")]


def main():
    puzzle = Puzzle(year=2021, day=8)
    submit(return_solution(split_input(puzzle.input_data)), part="a", day=8, year=2021)


if __name__ == '__main__':
    main()
