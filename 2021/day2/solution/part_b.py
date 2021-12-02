from aocd.models import Puzzle
from aocd import submit


def forward(pos, length):
    pos[1] += length
    pos[2] += pos[0] * length


def down(pos, length):
    pos[0] += length


def up(pos, length):
    pos[0] -= length


move = {"forward": forward, "down": down, "up": up}


def return_solution(puzzle):
    pos = [0, 0, 0]
    [move[direction[0]](pos, int(direction[1])) for direction in [a.split() for a in puzzle.split("\n")]]

    return pos[1] * pos[2]


def main():
    puzzle = Puzzle(year=2021, day=2)
    submit(return_solution(puzzle.input_data), part="b", day=2, year=2021)


if __name__ == '__main__':
    main()
