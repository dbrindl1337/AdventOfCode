from aocd.models import Puzzle
from aocd import submit


def calculate_levels(cols, sensor, compare):
    mask = 0b0
    for i in range(0, cols + 1):
        if len(sensor) == 1:
            return sensor[0]
        mask <<= 1
        bit_pos = cols - i - 1
        if compare(sum([((2**bit_pos & row) >> bit_pos) for row in sensor]), len(sensor) / 2):
            mask += 1
        sensor = list(filter(lambda x: (x >> bit_pos) % 2 == mask % 2, sensor))


def return_solution(puzzle):
    cols = len("{0:b}".format(max(puzzle)))

    oxygen = calculate_levels(cols, puzzle, lambda x, y: x >= y)
    carbon = calculate_levels(cols, puzzle, lambda x, y: x < y)

    return oxygen * carbon


def split_input_into_numbers(puzzle):
    return [int(i, 2) for i in puzzle.split("\n")]


def main():
    puzzle = Puzzle(year=2021, day=3)
    submit(return_solution(split_input_into_numbers(puzzle.input_data)), part="b", day=3, year=2021)


if __name__ == '__main__':
    main()
