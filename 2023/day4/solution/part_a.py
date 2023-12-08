from aocd.models import Puzzle
from aocd import submit

import re


def return_solution(cards):
    s = sum([int(2**(len(card[0] & card[1]) - 1)) for card in cards])
    return s


def split_input(puzzle):
    cards = [[set(re.split(r'\s+', number)) for number in re.sub(r'Card \d+: ', "", card).split(" | ")] for card in puzzle.split("\n")]
    return cards


def main():
    puzzle = Puzzle(year=2023, day=4)
    submit(return_solution(split_input(puzzle.input_data)), part="a", day=4, year=2023)


if __name__ == '__main__':
    main()
