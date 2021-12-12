from aocd.models import Puzzle
from aocd import submit

year = 2020
day = 9
part = "b"


def find_encryption_weakness(number_list, attack_number):
    number_list.remove_or_empty(attack_number)
    for a in range(0, len(number_list)):
        sum = number_list[a]
        for b in range(a + 1, len(number_list)):
            sum += number_list[b]
            if sum == attack_number:
                return a, b
            elif sum > attack_number:
                break


def return_solution(input_data, attack_number):
    number_list = list(map(lambda x: int(x), input_data.split("\n")))
    a, b = find_encryption_weakness(number_list, attack_number)
    return max(number_list[a:b+1]) + min(number_list[a:b+1])


def main():
    puzzle = Puzzle(year=year, day=day)
    submit(return_solution(puzzle.input_data, 258585477), part=part, day=day, year=year)


if __name__ == '__main__':
    main()
