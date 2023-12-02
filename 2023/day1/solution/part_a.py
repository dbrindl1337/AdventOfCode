from aocd.models import Puzzle
from aocd import submit


def get_sum_of_end_numbers(line):
    numbers = list(filter(lambda n: n.isnumeric(), line))
    return int(numbers[0] + numbers[-1])


def return_solution(lines):
    return sum([get_sum_of_end_numbers(line) for line in lines])


def split_input(puzzle):
    lines = puzzle.split("\n")
    return lines


def main():
    puzzle = Puzzle(year=2023, day=1)
    submit(return_solution(split_input(puzzle.input_data)), part="a", day=1, year=2023)


if __name__ == '__main__':
    main()
