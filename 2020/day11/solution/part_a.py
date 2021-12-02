from aocd.models import Puzzle
from aocd import submit

year = 2020
day = 11
part = "a"

row_length = 0
col_length = 0
seats = ""


def state_changed(new_seat_state):
    return seats != new_seat_state


def count_occupied_seats():
    return seats.count("#")


def get_seat(seat_pos):
    return seats[seat_pos // row_length + (seat_pos % row_length)]


def is_occupied(seat_pos):
    if 0 > seat_pos or seat_pos >= len(seats):
        return 0
    elif seats[seat_pos] == "#":
        return 1
    else:
        return 0


def is_empty(seat_pos):
    if 0 > seat_pos or seat_pos >= len(seats):
        return 0
    elif seats[seat_pos] == "L":
        return 1
    else:
        return 0


def get_occupied_adjacent_seat_count(seat_pos):
    
    return is_occupied(seat_pos + 1) + is_occupied(seat_pos - 1) + is_occupied(seat_pos + row_length) + is_occupied(seat_pos - row_length) \
           + is_occupied(seat_pos + 1 + row_length) + is_occupied(seat_pos - 1 + row_length) \
           + is_occupied(seat_pos + 1 - row_length) + is_occupied(seat_pos - 1 - row_length)


def simulate_round():
    seats_after = ""

    for seat_index in range(0, len(seats)):
        if is_empty(seat_index) == 1:
            seats_after += "#"
        elif is_occupied(seat_index) == 1 and get_occupied_adjacent_seat_count(seat_index) >= 4:
            seats_after += "L"
        else:
            seats_after += seats[seat_index]

    return seats_after


def return_solution(input_data):
    global seats, row_length, col_length
    row_length = input_data.index("\n")
    seats = input_data.replace("\n", "")
    col_length = len(input_data) / row_length

    new_seat_state = simulate_round()

    while state_changed(new_seat_state):
        seats = new_seat_state
        new_seat_state = simulate_round()

    return count_occupied_seats()


def main():
    puzzle = Puzzle(year=year, day=day)
    submit(return_solution(puzzle.input_data), part=part, day=day, year=year)


if __name__ == '__main__':
    main()
