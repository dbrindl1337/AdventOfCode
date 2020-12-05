from aocd.models import Puzzle
from aocd import submit

year = 2020
day = 5
part = "a"


def get_seat_id(seat):
    number = 0
    for n in range(0, len(seat)):
        if seat[n] == "B" or seat[n] == "R":
            number += 1 << n
    return number


def return_solution(input_data):
    seat_list = input_data.split("\n")
    return max(map(get_seat_id, [a[::-1] for a in seat_list]))


def main():
    puzzle = Puzzle(year=year, day=day)
    submit(return_solution(puzzle.input_data), part=part, day=day, year=year)


if __name__ == '__main__':
    main()
