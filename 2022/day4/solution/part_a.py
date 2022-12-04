from aocd.models import Puzzle
from aocd import submit


def return_solution(elves):

    fully_contained = 0

    for pair in elves:
        if pair[1][0] <= pair[0][0] and pair[1][1] >= pair[0][1]:
            fully_contained += 1
        elif pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][1]:
            fully_contained += 1

    return fully_contained


def split_input(puzzle):
    sections = [[[int(section) for section in pair.split("-")] for pair in line.split(",")] for line in puzzle.split("\n")]

    return sections


def main():

    puzzle = Puzzle(year=2022, day=4)
    submit(return_solution(split_input(puzzle.input_data)), part="a", day=4, year=2022)


if __name__ == '__main__':
    main()
