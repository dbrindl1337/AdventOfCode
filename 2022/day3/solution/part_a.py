from aocd.models import Puzzle
from aocd import submit


def prioritize(department):
    return [ord(i) - 38 if i < "a" else ord(i) - 96 for i in department]


def return_solution(rucksacks):

    sum_of_items = 0

    for rucksack in rucksacks:
        first_compartment = set(rucksack[0])
        second_compartment = set(rucksack[1])
        duplicates = [item if item in second_compartment else 0 for item in first_compartment]
        sum_of_items += sum(duplicates)

    return sum_of_items


def split_input(puzzle):
    rucksacks = [(prioritize(rucksack[:len(rucksack)//2]), prioritize(rucksack[len(rucksack)//2:])) for rucksack in puzzle.split("\n")]
    return rucksacks


def main():
    puzzle = Puzzle(year=2022, day=3)
    submit(return_solution(split_input(puzzle.input_data)), part="a", day=3, year=2022)


if __name__ == '__main__':
    main()
