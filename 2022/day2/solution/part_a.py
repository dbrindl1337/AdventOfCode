from aocd.models import Puzzle
from aocd import submit


def return_solution(matches):
    points_from_shapes = sum([match[1] for match in matches])
    points_from_matches = sum([6 if match[0] - match[1] == -1 or match[0] - (match[1] - 23) == 2
                               else 3 if match[0] == match[1]
                                else 0
                               for match in matches])

    return points_from_shapes + points_from_matches


def split_input(puzzle):
    a = [list(map(lambda x: [ord(x[0]) - 64, ord(x[1]) - 87], [i.split(" ")])) for i in puzzle.split("\n")]
    b = [item for lines in a for item in lines]
    return b


def main():
    puzzle = Puzzle(year=2022, day=2)
    submit(return_solution(split_input(puzzle.input_data)), part="a", day=2, year=2022)


if __name__ == '__main__':
    main()
