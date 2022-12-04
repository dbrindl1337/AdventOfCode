from aocd.models import Puzzle
from aocd import submit


def return_solution(elves):
    calorie_list = [sum(elf) for elf in elves]
    calorie_list.sort(reverse=True)
    return sum(calorie_list[0:3])


def split_input(puzzle):
    elves = puzzle.split("\n\n")

    return [[int(calories) for calories in elf.split("\n")] for elf in elves]


def main():
    puzzle = Puzzle(year=2022, day=1)
    submit(return_solution(split_input(puzzle.input_data)), part="b", day=1, year=2022)


if __name__ == '__main__':
    main()
