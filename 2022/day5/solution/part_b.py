import re

from aocd.models import Puzzle
from aocd import submit


def return_solution(config):

    stacks = config[0]
    instructions = config[1]

    for instruction in instructions:
        move = []
        for i in range(0, int(instruction[0])):
            move.append(stacks[instruction[1]].pop())
        move.reverse()
        stacks[instruction[2]].extend(move)

    return ''.join([stack.pop() for stack in stacks.values()])


def split_input(puzzle):
    crates, instructions = puzzle.split("\n\n")

    crates = crates.split("\n")

    crates = [[re.sub("[ \[\]]", "", row[i:i+3]) for row in crates] for i in range(0, len(crates[0]) + 1, 4)]

    stacks = {}

    for crate in crates:
        stacks[crate[-1]] = list(filter(len, crate[:-1]))[::-1]

    instructions = [re.findall("\\d+", instruction) for instruction in instructions.split("\n")]

    return stacks, instructions


def main():
    puzzle = Puzzle(year=2022, day=5)
    submit(return_solution(split_input(puzzle.input_data)), part="b", day=5, year=2022)


if __name__ == '__main__':
    main()
