from aocd.models import Puzzle
from aocd import submit

year = 2020
day = 11
part = "b"


def return_solution(input_data):
    return


def main():
    puzzle = Puzzle(year=year, day=day)
    submit(return_solution(puzzle.input_data), part=part, day=day, year=year)


if __name__ == '__main__':
    main()
