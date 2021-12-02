from aocd.models import Puzzle
from aocd import submit

year = 2020
day = 10
part = "b"

paths = {}


def combinations(adapters, index):
    if index == len(adapters) - 1:
        return 1
    if index in paths:
        return paths[index]

    possible_connections = list(filter(lambda x: x - adapters[index] <= 3,
                                       adapters[index + 1:max(len(adapters), index + 3)]))
    path_count = sum([combinations(adapters, index + offset + 1) for offset in range(0, len(possible_connections))])
    paths[index] = path_count

    return path_count


def calc_adapters(adapters):
    adapters.append(0)
    return combinations(sorted(adapters), 0)


def return_solution(input_data):
    return calc_adapters(list(map(lambda x: int(x), input_data.split("\n"))))


def main():
    puzzle = Puzzle(year=year, day=day)
    submit(return_solution(puzzle.input_data), part=part, day=day, year=year)


if __name__ == '__main__':
    main()
