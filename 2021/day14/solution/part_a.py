from collections import defaultdict

from aocd.models import Puzzle
from aocd import submit


def return_solution(instructions, iteration_count):
    template = instructions[0]
    rules = instructions[1]

    new_polymer = ""

    for k in range(0, iteration_count):
        for i in range(0, len(template) - 1):
            base = template[i:i + 2]
            new_polymer += base[0]
            new_polymer += rules[base]
        new_polymer += template[len(template) - 1]
        template = new_polymer
        new_polymer = ""

    distribution = defaultdict(lambda: 0)

    for char in template:
        distribution[char] += 1

    return max(distribution.values()) - min(distribution.values())


def split_input(puzzle):
    lines = puzzle.split("\n\n")

    template = lines[0]

    lines = dict([line.split(" -> ") for line in lines[1].split("\n")])
    return template, lines


def main():
    puzzle = Puzzle(year=2021, day=14)
    submit(return_solution(split_input(puzzle.input_data), 10), part="a", day=14, year=2021)


if __name__ == '__main__':
    main()
