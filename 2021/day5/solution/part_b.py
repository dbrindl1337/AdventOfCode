from aocd.models import Puzzle
from aocd import submit
from collections import defaultdict


def is_diagonal(line):
    return line[0][0] != line[1][0] and line[0][1] != line[1][1]


def is_increase_x(line):
    return line[0][0] != line[1][0]


def calc_range(line):
    start = 0
    stop = 0

    if is_increase_x(line):
        if line[0][0] > line[1][0]:
            start = line[1][0]
            stop = line[0][0]
        else:
            start = line[0][0]
            stop = line[1][0]
    else:
        if line[0][1] > line[1][1]:
            start = line[1][1]
            stop = line[0][1]
        else:
            start = line[0][1]
            stop = line[1][1]

    return range(start, stop + 1)


def fill_lines_in_map(line, line_map):
    if is_diagonal(line):
        for i in range(0, abs(line[0][0] - line[1][0]) + 1):
            if line[0][0] > line[1][0] and line[0][1] > line[1][1]:
                line_map[(line[0][0] - i, line[0][1] - i)] += 1
            elif line[0][0] > line[1][0] and line[0][1] < line[1][1]:
                line_map[(line[0][0] - i, line[0][1] + i)] += 1
            elif line[0][0] < line[1][0] and line[0][1] > line[1][1]:
                line_map[(line[0][0] + i, line[0][1] - i)] += 1
            elif line[0][0] < line[1][0] and line[0][1] < line[1][1]:
                line_map[(line[0][0] + i, line[0][1] + i)] += 1
    else:
        for i in calc_range(line):
            if is_increase_x(line):
                line_map[(i, line[0][1])] += 1
            else:
                line_map[(line[0][0], i)] += 1


def return_solution(puzzle):
    line_map = defaultdict(lambda: 0)

    for line in puzzle:
        fill_lines_in_map(line, line_map)

    return len(list(filter(lambda x: x > 1, line_map.values())))


def split_input(puzzle):
    lines = [[list(map(lambda i: int(i), pos.split(","))) for pos in line.split(" -> ")] for line in puzzle.split("\n")]
    return lines


def main():
    puzzle = Puzzle(year=2021, day=5)
    submit(return_solution(split_input(puzzle.input_data)), part="b", day=5, year=2021)


if __name__ == '__main__':
    main()
