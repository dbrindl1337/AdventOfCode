from aocd.models import Puzzle
from aocd import submit


def return_solution(puzzle):
    opening_symbols = {'<', '{', '[', '('}
    closing_symbols = {'>', '}', ']', ')'}
    mapping = {'<': '>', '>': '<',
               '{': '}', '}': '{',
               '[': ']', ']': '[',
               '(': ')', ')': '('
               }
    point_mapping = {
        '>': 25137,
        '}': 1197,
        ']': 57,
        ')': 3
    }

    sum = 0

    stack = []
    for line in puzzle:
        for i, char in enumerate(line):
            if char in opening_symbols:
                stack.append(char)
            elif char in closing_symbols:
                next_char = stack.pop()
                if mapping[char] == next_char:
                    continue
                else:
                    sum += point_mapping[char]
                    print(f"expected {char} at {i}")
        print(f"stack size: {len(stack)}")
        stack = []
    return sum


def split_input(puzzle):
    return puzzle.split("\n")


def main():
    puzzle = Puzzle(year=2021, day=10)
    print(return_solution(split_input(puzzle.input_data)))
    submit(return_solution(split_input(puzzle.input_data)), part="a", day=10, year=2021)


if __name__ == '__main__':
    main()
