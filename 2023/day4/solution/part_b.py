from collections import defaultdict

from aocd.models import Puzzle
from aocd import submit

import re


def return_solution(cards):

    for index, card in enumerate(cards):
        for i in range(index, index + len(set(card[0]) & set(card[1]))):
            cards[list(cards.keys())[i + 1]] += cards[list(cards.keys())[index]]
    return sum(cards.values())


def split_input(puzzle):
    cards = {tuple(tuple(re.split(r'\s+', number)) for number in re.sub(r'Card \d+: ', "", card).strip().split(" | ")): 1 for
             card in
             puzzle.split("\n")}
    return cards


def main():
    puzzle = Puzzle(year=2023, day=4)
    submit(return_solution(split_input(puzzle.input_data)), part="b", day=4, year=2023)


if __name__ == '__main__':
    main()
