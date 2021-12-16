from collections import defaultdict, Counter
from functools import lru_cache

from aocd.models import Puzzle
from aocd import submit

# distribution = defaultdict(lambda: 0)
rules = dict()
max_depth = 0


@lru_cache(maxsize=4096)
def calc_new_polymer(polymer, depth):
    distribution = defaultdict(lambda: 0)
    if depth == max_depth:
        distribution[polymer[0]] += 1
        return distribution

    polymer = polymer[0] + rules[polymer] + polymer[1]
    print(f"poly: {polymer}, depth: {depth}")
    c = Counter()

    for i in range(len(polymer) - 1):
        c += Counter(calc_new_polymer(polymer[i:i + 2], depth + 1))

    return dict(c)


def return_solution(instructions, iteration_count):
    global rules
    global max_depth
    max_depth = iteration_count

    polymer, rules = instructions

    c = Counter()

    for i in range(len(polymer) - 1):
        c += Counter(calc_new_polymer(polymer[i:i + 2], 0))

    c[polymer[-1]] += 1

    return max(c.values()) - min(c.values())


def split_input(puzzle):
    lines = puzzle.split("\n\n")

    template = lines[0]

    lines = dict([line.split(" -> ") for line in lines[1].split("\n")])
    return template, lines


def main():
    puzzle = Puzzle(year=2021, day=14)
    print(return_solution(split_input(puzzle.input_data), 40))
    #submit(return_solution(split_input(puzzle.input_data), 40), part="b", day=14, year=2021)


if __name__ == '__main__':
    main()
