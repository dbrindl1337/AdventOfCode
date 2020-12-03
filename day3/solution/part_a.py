from aocd.models import Puzzle
from aocd import submit

year = 2020
day = 3
part = "a"


def is_tree_hit(horizontal_data):
    line, hitting_point = horizontal_data
    return line[hitting_point] == "#"


def get_hits_functional(input_data):
    area = input_data.split("\n")[1:]
    hitting_points = [((point + 1) * 3) % len(area[0]) for point in range(0, len(area), 1)]
    area = zip(area, hitting_points)
    return len([hit for hit in map(is_tree_hit, area) if hit])


def get_hits(input_data):
    area = input_data.split("\n")
    trees_hit = 0
    horizontal = 3
    for vertical in range(1, len(area) - 1):
        if area[vertical][horizontal] == "#":
            trees_hit += 1
        horizontal += 3
        horizontal %= len(area[0])
    return trees_hit


def return_solution(input_data):
    return get_hits(input_data)


def main():
    puzzle = Puzzle(year=year, day=day)
    submit(return_solution(puzzle.input_data), part=part, day=day, year=year)


if __name__ == '__main__':
    main()
