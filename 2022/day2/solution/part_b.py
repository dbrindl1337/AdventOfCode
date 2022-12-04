from aocd.models import Puzzle
from aocd import submit


def get_shape_points(match):
    match match[1]:
        case 1:
            return 3 if match[0] + 2 == 3 else (match[0] + 2) % 3
        case 2:
            return match[0]
        case 3:
            return match[0] % 3 + 1


def return_solution(matches):
    points_from_shapes = sum([get_shape_points(match) for match in matches])

    outcomes = {
        1: 0,
        2: 0,
        3: 0
    }

    for match in matches:
        outcomes[match[1]] += 1

    points_from_matches = outcomes[2] * 3 + outcomes[3] * 6

    return points_from_shapes + points_from_matches


def split_input(puzzle):
    a = [list(map(lambda x: [ord(x[0]) - 64, ord(x[1]) - 87], [i.split(" ")])) for i in puzzle.split("\n")]
    b = [item for lines in a for item in lines]
    return b


def main():
    puzzle = Puzzle(year=2022, day=2)
    submit(return_solution(split_input(puzzle.input_data)), part="b", day=2, year=2022)


if __name__ == '__main__':
    main()
