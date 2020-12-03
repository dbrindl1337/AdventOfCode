from aocd.models import Puzzle
from aocd import submit
import re


def is_valid(password):
    first, second, char, password = re.split("-| |: ", password)
    return (password[int(first) - 1] == char) ^ (password[int(second) - 1] == char)


def return_solution(input_data):
    passwords = input_data.split("\n")
    result = filter(lambda x: is_valid(x), passwords)
    return len(list(result))


def main():
    puzzle = Puzzle(year=2020, day=2)
    submit(return_solution(puzzle.input_data), part="b", day=2, year=2020)


if __name__ == '__main__':
    main()
