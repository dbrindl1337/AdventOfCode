import re

from aocd.models import Puzzle
from aocd import submit


def is_part(point):
    return point.isnumeric()


def get_8_kernel():
    return [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def get_neighbor_number_positions(position, engine):
    positions = []
    for k in get_8_kernel():
        x = position[0] + k[0]
        y = position[1] + k[1]
        if engine[x][y].isnumeric():
            positions.append((x, y))
    return positions


def return_solution(numbers):
    engine = [[*line] for line in numbers]
    number_map = {}
    part_indicator_map = {}
    parts = set()

    for row, line in enumerate(numbers):
        numbers = re.finditer(r'\d+', line)
        part_indicators = re.finditer(r'[^0-9.]', line)
        for number in numbers:
            for i in range(number.span()[0], number.span()[1]):
                number_map[(row, i)] = int(number.group())
        for part_indicator in part_indicators:
            for i in range(part_indicator.span()[0], part_indicator.span()[1]):
                part_indicator_map[(row, i)] = part_indicator.group()

    for part_indicator in part_indicator_map:
        part_numbers = get_neighbor_number_positions(part_indicator, engine)
        for part_number in part_numbers:
            parts.add(number_map[part_number])

    return sum(parts)


def split_input(puzzle):
    lines = puzzle.split("\n")
    return lines


def main():
    puzzle = Puzzle(year=2023, day=3)
    submit(return_solution(split_input(puzzle.input_data)), part="a", day=3, year=2023)


if __name__ == '__main__':
    main()
