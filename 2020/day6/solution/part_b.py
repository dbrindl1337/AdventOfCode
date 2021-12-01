from functools import reduce

from aocd.models import Puzzle
from aocd import submit

year = 2020
day = 6
part = "b"


def count_unique(answers):
    return len(reduce(lambda x, y: set(x).intersection(set(y)), answers))


def sum_up_group_answers(group_list):
    return sum([count_unique(group.split("\n")) for group in group_list])


def return_solution(input_data):
    return sum_up_group_answers(input_data.split("\n\n"))


def main():
    puzzle = Puzzle(year=year, day=day)
    submit(return_solution(puzzle.input_data), part=part, day=day, year=year)


if __name__ == '__main__':
    main()
