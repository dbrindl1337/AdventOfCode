from aocd.models import Puzzle
from aocd import submit

year = 2020
day = 10
part = "a"


def calc_adapters(adapters):
    adapters.append(0)
    adapters = sorted(adapters)
    one_jolt = 0
    three_jolt = 0
    else_jolt = 0

    for i in range(0, len(adapters) - 1):
        if adapters[i + 1] - adapters[i] == 1:
            one_jolt += 1
        elif adapters[i + 1] - adapters[i] == 3:
            three_jolt += 1
        else:
            else_jolt += 1

    return one_jolt * (three_jolt + 1)


def return_solution(input_data):
    return calc_adapters(list(map(lambda x: int(x), input_data.split("\n"))))


def main():
    puzzle = Puzzle(year=year, day=day)
    submit(return_solution(puzzle.input_data), part=part, day=day, year=year)


if __name__ == '__main__':
    main()
