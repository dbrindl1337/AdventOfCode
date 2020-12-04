from aocd.models import Puzzle
from aocd import submit
import re

year = 2020
day = 4
part = "b"


def to_passport_map(passport):
    passport_specs = passport.split()
    passport_map = {}
    for spec in passport_specs:
        key, value = spec.split(":")
        passport_map[key] = value
    return passport_map


def is_passport_valid(passport):
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    for field in required_fields:
        if field not in passport:
            return False

    color_pattern = re.compile("#([0-9]|[a-f]){6}")
    valid_eye_colors = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}

    byr = int(passport["byr"])
    iyr = int(passport["iyr"])
    eyr = int(passport["eyr"])
    hgt = int(passport["hgt"][:-2])
    hgt_unit = passport["hgt"][-2:]
    hcl = passport["hcl"]
    ecl = passport["ecl"]
    pid = passport["pid"]

    if not(1920 <= byr <= 2002):
        return False

    if not(2010 <= iyr <= 2020):
        return False

    if not(2020 <= eyr <= 2030):
        return False

    if hgt_unit == "cm":
        if not(150 <= hgt <= 193):
            return False
    elif hgt_unit == "in":
        if not(59 <= hgt <= 76):
            return False

    if not re.match(color_pattern, hcl):
        return False

    if ecl not in valid_eye_colors:
        return False

    if not(len(pid) == 9 and pid.isnumeric()):
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
