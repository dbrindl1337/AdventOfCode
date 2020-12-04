from aocd.models import Puzzle
from aocd import submit

year = 2020
day = 4
part = "a"


def to_passport_map(passport):
    passport_specs = passport.split()
    passport_map = {}
    for spec in passport_specs:
        key, value = spec.split(":")
        passport_map[key] = value
    return passport_map


def is_passport_valid(passport):
    required_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

    for field in required_fields:
        if field not in passport:
            return False

    return True


def count_valid_passwords(input_data):
    passports = input_data.split("\n\n")
    list_of_passports = map(to_passport_map, passports)
    return len(list(filter(is_passport_valid, list_of_passports)))


def return_solution(input_data):
    return count_valid_passwords(input_data)


def main():
    puzzle = Puzzle(year=year, day=day)
    submit(return_solution(puzzle.input_data), part=part, day=day, year=year)


if __name__ == '__main__':
    main()
