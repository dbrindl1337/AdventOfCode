from functools import reduce

from aocd.models import Puzzle
from aocd import submit

import re


def return_solution(games):
    game_map = {}
    powers = []

    for game in games:
        for sub in game:
            for val in sub:
                game_map.setdefault(val[1], 0)
                game_map[val[1]] = max(game_map[val[1]], val[0])
        powers.append(reduce((lambda x, y: x * y), game_map.values()))
        game_map = {}

    return sum(powers)


def split_input(puzzle):
    lines = [[[(int(sub.split(" ")[0]), sub.split(" ")[1]) for sub in game.split(", ")] for game in
              re.sub("Game [0-9]+: ", "", line).split("; ")] for line in puzzle.split("\n")]
    return lines


def main():
    puzzle = Puzzle(year=2023, day=2)
    submit(return_solution(split_input(puzzle.input_data)), part="b", day=2, year=2023)


if __name__ == '__main__':
    main()
