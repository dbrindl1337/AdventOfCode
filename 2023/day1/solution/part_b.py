from collections import OrderedDict

from aocd.models import Puzzle
from aocd import submit


def transform_lines(lines):
    transformed_lines = []
    for line in lines:
        t_line = line.replace("one", "o1e").replace("two", "t2o").replace("three", "t3e").replace("four", "f4r").replace(
            "five", "f5e").replace("six", "s6x").replace("seven", "s7n").replace("eight", "e8t").replace("nine", "n9e")
        transformed_lines.append(t_line)
    return transformed_lines


def get_sum_of_end_numbers(line):
    numbers = list(filter(lambda n: n.isnumeric(), line))
    return int(numbers[0] + numbers[-1])


def return_solution(lines):
    transformed_lines = transform_lines(lines)
    return sum([get_sum_of_end_numbers(line) for line in transformed_lines])


def split_input(puzzle):
    lines = puzzle.split("\n")
    return lines


def main():
    puzzle = Puzzle(year=2023, day=1)

    submit(return_solution(split_input(puzzle.input_data)), part="b", day=1, year=2023)


if __name__ == '__main__':
    main()
