from aocd.models import Puzzle
from aocd import submit


def remove_or_empty(rset, element):
    if rset.issuperset(element):
        return rset - element
    return set()


def get_configuration(hints):
    numbers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    line_ids = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    numbers[1] = [*map(lambda s: set(s), (filter(lambda x: len(x) == 2, hints)))][0]
    numbers[4] = [*map(lambda s: set(s), (filter(lambda x: len(x) == 4, hints)))][0]
    numbers[7] = [*map(lambda s: set(s), (filter(lambda x: len(x) == 3, hints)))][0]
    numbers[8] = [*map(lambda s: set(s), (filter(lambda x: len(x) == 7, hints)))][0]

    line_ids[0] = numbers[7] - numbers[1]

    numbers[9] = [*map(lambda s: set(s), (filter(lambda x: len(x) == 6 and remove_or_empty(set(x), line_ids[0]).issuperset(numbers[4]), hints)))][0]

    line_ids[7] = numbers[9] - (numbers[4] | line_ids[0])

    numbers[3] = [*map(lambda s: set(s), (filter(lambda x: len(x) == 5 and remove_or_empty(remove_or_empty(set(x), line_ids[0]), line_ids[7]).issuperset(numbers[1]), hints)))][0]

    line_ids[3] = numbers[3] - (numbers[1] | line_ids[0] | line_ids[7])

    numbers[0] = [*map(lambda s: set(s), (filter(lambda x: len(x) == 6 and set(x).issuperset(remove_or_empty(numbers[8], line_ids[3])), hints)))][0]

    numbers[6] = [*map(lambda s: set(s), (filter(lambda x: len(x) == 6 and set(x) != numbers[0] and set(x) != numbers[9], hints)))][0]

    line_ids[4] = numbers[8] - numbers[9]

    numbers[5] = numbers[6] - line_ids[4]

    numbers[2] = [*map(lambda s: set(s), (filter(lambda x: len(x) == 5 and set(x) != numbers[3] and set(x) != numbers[5], hints)))][0]

    return numbers


def apply_configuration(numbers, config):
    sum = 0

    for number in numbers:
        sum *= 10
        sum += config.index(set(number))

    return sum


def return_solution(puzzle):
    hints = [hint.split() for hint in [p[0] for p in puzzle]]
    numbers = [number.split() for number in [p[1] for p in puzzle]]

    return_sum = 0

    for i, hint in enumerate(hints):
        config = get_configuration(hint)
        return_sum += apply_configuration(numbers[i], config)

    return return_sum


def split_input(puzzle):
    return [line.split(" | ") for line in puzzle.split("\n")]


def main():
    puzzle = Puzzle(year=2021, day=8)
    submit(return_solution(split_input(puzzle.input_data)), part="b", day=8, year=2021)


if __name__ == '__main__':
    main()
