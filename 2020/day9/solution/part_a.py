from aocd.models import Puzzle
from aocd import submit

year = 2020
day = 9
part = "a"


def find_first_invalid_number(number_list, preamble_length):
    number_pool = set(number_list[:preamble_length])

    for index in range(preamble_length, len(number_list)):
        next_number_to_remove = number_list[index - preamble_length]
        found = False
        for pool_number in number_pool:
            found |= (number_list[index] - pool_number) in number_pool
        if not found:
            return number_list[index]
        number_pool.remove(next_number_to_remove)
        number_pool.add(number_list[index])


def return_solution(input_data, preamble_length):
    return find_first_invalid_number(list(map(lambda x: int(x), input_data.split("\n"))), preamble_length)


def main():
    puzzle = Puzzle(year=year, day=day)
    submit(return_solution(puzzle.input_data, 25), part=part, day=day, year=year)


if __name__ == '__main__':
    main()
