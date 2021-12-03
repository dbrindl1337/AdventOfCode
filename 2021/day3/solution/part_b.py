from aocd.models import Puzzle
from aocd import submit


def return_mask(puzzle):
    pass


def return_solution(puzzle):
    cols = len("{0:b}".format(max(puzzle)))
    rows = len(puzzle)
    mask = 0b0

    filtered_puzzle = puzzle

    for i in range(0, cols):
        mask <<= 1
        bit_pos = cols - i - 1
        if sum([((2**bit_pos & row) >> bit_pos) for row in filtered_puzzle]) >= rows // 2:
            mask += 1
        filtered_puzzle = list(filter(lambda x: (x & (mask << bit_pos)) >= (mask << bit_pos), filtered_puzzle))
    return


def split_input_into_numbers(puzzle):
    return [int(i, 2) for i in puzzle.split("\n")]


def main():
    puzzle = Puzzle(year=2021, day=3)
    submit(return_solution(split_input_into_numbers(puzzle.input_data)), part="b", day=3, year=2021)


if __name__ == '__main__':
    main()
