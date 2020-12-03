from functools import reduce

from aocd.models import Puzzle
from aocd import submit

year = 2020
day = 3
part = "b"


def is_tree_hit(horizontal_data):
    line, hitting_point = horizontal_data
    return line[hitting_point] == "#"


def get_hits(input_data, slope):
    area = input_data.split("\n")[slope[1]:]
    hitting_points = [((point + 1) * slope[0]) % len(area[0]) for point in range(0, len(area), 1)]
    area = list(zip(area[::slope[1]], hitting_points))
    return len([hit for hit in map(is_tree_hit, area) if hit])


def return_solution(input_data, slopes):
    map(get_hits, (input_data,) * len(slopes), slopes)
    return reduce((lambda x, y: x * y), map(get_hits, (input_data,) * len(slopes), slopes))


def main():
    puzzle = Puzzle(year=year, day=day)
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    submit(return_solution(puzzle.input_data, slopes), part=part, day=day, year=year)


if __name__ == '__main__':
    main()
