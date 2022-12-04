from aocd.models import Puzzle
from aocd import submit


def prioritize(department):
    return [ord(i) - 38 if i < "a" else ord(i) - 96 for i in department]


def return_solution(rucksacks):

    sum_of_items = 0

    for n in range(0, len(rucksacks), 3):
        first_rucksack = set(rucksacks[n])
        second_rucksack = set(rucksacks[n + 1])
        third_rucksack = set(rucksacks[n + 2])

        duplicates_1_2 = [item if item in first_rucksack else 0 for item in second_rucksack]
        duplicates_1_2__3 = [item if item in third_rucksack else 0 for item in duplicates_1_2]

        sum_of_items += sum(duplicates_1_2__3)

    return sum_of_items


def split_input(puzzle):
    rucksacks = [(prioritize(rucksack)) for rucksack in puzzle.split("\n")]
    return rucksacks


def main():
    puzzle = Puzzle(year=2022, day=3)
    submit(return_solution(split_input(puzzle.input_data)), part="b", day=3, year=2022)


if __name__ == '__main__':
    main()
