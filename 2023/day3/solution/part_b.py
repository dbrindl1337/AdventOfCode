import re

from aocd.models import Puzzle
from aocd import submit


def is_part(point):
    return point.isnumeric()


def get_8_kernel():
    return [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def get_gears(position, number_map, engine):
    first_number = 0
    second_number = 0

    for k in get_8_kernel():
        x = position[0] + k[0]
        y = position[1] + k[1]
        if x < 0 or y < 0 or x > len(engine) - 1 or y > len(engine[0]) - 1:
            continue
        if engine[x][y].isnumeric():
            if first_number == 0:
                first_number = number_map[(x, y)]
                continue
            if second_number == 0 and number_map[(x, y)] != first_number:
                second_number = number_map[(x, y)]

    return first_number * second_number


def return_solution(numbers):
    engine = [[*line] for line in numbers]
    number_map = {}
    gear_sum = 0
    nums = list(numbers)

    for row, line in enumerate(nums):
        numbers = re.finditer(r'\d+', line)
        for number in numbers:
            for i in range(number.span()[0], number.span()[1]):
                number_map[(row, i)] = int(number.group())

    for row, line in enumerate(nums):
        part_indicators = re.finditer(r'\*', line)
        for part_indicator in part_indicators:
            gear_sum += get_gears((row, part_indicator.span()[0]), number_map, engine)

    return gear_sum


def split_input(puzzle):
    lines = puzzle.split("\n")
    return lines


def main():
    puzzle = Puzzle(year=2023, day=3)
    submit(return_solution(split_input(puzzle.input_data)), part="b", day=3, year=2023)


if __name__ == '__main__':
    main()
