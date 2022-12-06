from aocd.models import Puzzle
from aocd import submit


def return_solution(lines):
    window_size = 4
    for i in range(0, len(lines) - window_size):
        if len(set(lines[i:i+window_size])) == window_size:
            return i + window_size


def split_input(puzzle):
    return puzzle


def main():
    puzzle = Puzzle(year=2022, day=6)
    submit(return_solution(split_input(puzzle.input_data)), part="a", day=6, year=2022)


if __name__ == '__main__':
    main()
