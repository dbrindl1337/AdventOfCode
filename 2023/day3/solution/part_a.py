import re

from aocd.models import Puzzle
from aocd import submit


def is_part(point):
    return point.isnumeric()


def get_8_kernel():
    return [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def exclude(position, engine):
    for k in get_8_kernel():
        x = position[0] + k[0]
        y = position[1] + k[1]
        if x < 0 or y < 0 or x > len(engine) - 1 or y > len(engine[0]) - 1:
            continue
        if not engine[x][y].isnumeric() and engine[x][y] != ".":
            return True
    return False


def return_solution(numbers):
    engine = [[*line] for line in numbers]
    number_map = {}
    part_indicator_map = {}
    parts = set()
    sum_numbers = 0

    for row, line in enumerate(numbers):
        numbers = re.finditer(r'\d+', line)
        part_indicators = re.finditer(r'[^0-9.]', line)
        for number in numbers:
            include = False
            for i in range(number.span()[0], number.span()[1]):
                include = include or exclude((row, i), engine)
            if include:
                sum_numbers += int(number.group())
    return sum_numbers


def split_input(puzzle):
    lines = puzzle.split("\n")
    return lines


def main():
    puzzle = Puzzle(year=2023, day=3)
    submit(return_solution(split_input(puzzle.input_data)), part="a", day=3, year=2023)


if __name__ == '__main__':
    main()
