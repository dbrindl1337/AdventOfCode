from aocd.models import Puzzle
from aocd import submit


def return_solution(report):
    entries = report.split("\n")
    for e in entries:
        for f in entries:
            for g in entries:
                if int(e) + int(f) + int(g) == 2020:
                    return int(e) * int(f) * int(g)


def main():
    puzzle = Puzzle(year=2020, day=1)
    submit(return_solution(puzzle.input_data), part="a", day=1, year=2020)


if __name__ == '__main__':
    main()
