from aocd.models import Puzzle
from aocd import submit


def return_solution(elves):
    overlapping = 0

    for pair in elves:
        if pair[0][1] >= pair[1][0] and pair[1][1] >= pair[0][0]:
            overlapping += 1

    return overlapping


def split_input(puzzle):
    sections = [[[int(section) for section in pair.split("-")] for pair in line.split(",")] for line in puzzle.split("\n")]

    return sections


def main():
    puzzle = Puzzle(year=2022, day=4)
    submit(return_solution(split_input(puzzle.input_data)), part="b", day=4, year=2022)


if __name__ == '__main__':
    main()
