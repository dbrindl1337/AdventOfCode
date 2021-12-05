from aocd.models import Puzzle
from aocd import submit


def return_solution(puzzle):
    numbers = puzzle[0]
    fields = puzzle[1]

    for number in numbers:
        for field in fields:
            row_index = 0
            for row in field:
                col_index = 0
                for column in row:
                    if column == number:
                        field[row_index][col_index] = -column
                    row_win = True
                    col_win = True
                    for check_column in row:
                        if check_column >= 0:
                            row_win = False
                            break
                    for check_row in [c[row_index] for c in field]:
                        if check_row >= 0:
                            col_win = False
                            break
                    if row_win:
                        field_sum = sum([sum([c if c > 0 else 0 for c in r]) for r in field])
                        return field_sum * number
                    elif col_win:
                        field_sum = sum([sum([c if c > 0 else 0 for c in r]) for r in field])
                        return field_sum * number
                    col_index += 1
                row_index += 1


def split_input(puzzle):
    split = puzzle.split("\n\n")
    numbers = [int(n) + 1 for n in split[0].split(",")]
    fields = [[[int(h) + 1 for h in g.split()] for g in f.split("\n")] for f in split[1:]]

    return numbers, fields


def main():
    puzzle = Puzzle(year=2021, day=4)
    submit(return_solution(split_input(puzzle.input_data)), part="a", day=4, year=2021)


if __name__ == '__main__':
    main()
