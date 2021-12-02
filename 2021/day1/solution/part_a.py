from aocd.models import Puzzle
from aocd import submit


def return_solution(floor_values):
    floor_level = floor_values.split("\n")
    floor_level = list(map(lambda x: int(x), floor_level))
    floor_level = list(zip(floor_level, floor_level[1:]))
    return sum(map(lambda x: 1 if x[1] > x[0] else 0, floor_level))


def main():
    puzzle = Puzzle(year=2021, day=1)
    submit(return_solution(puzzle.input_data), part="a", day=1, year=2021)


if __name__ == '__main__':
    main()
