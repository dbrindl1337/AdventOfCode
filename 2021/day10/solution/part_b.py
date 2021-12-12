from aocd.models import Puzzle
from aocd import submit


def calc_points(points):
    score = 0
    for point in points:
        score *= 5
        score += point
    return score


def return_solution(puzzle):
    opening_symbols = {'<', '{', '[', '('}
    closing_symbols = {'>', '}', ']', ')'}
    mapping = {'<': '>', '>': '<',
               '{': '}', '}': '{',
               '[': ']', ']': '[',
               '(': ')', ')': '('
               }
    point_mapping = {
        '>': 4,
        '}': 3,
        ']': 2,
        ')': 1
    }

    points = []

    stack = []
    for line in puzzle:
        error = False
        for i, char in enumerate(line):
            if char in opening_symbols:
                stack.append(char)
            elif char in closing_symbols:
                next_char = stack.pop()
                if mapping[char] == next_char:
                    continue
                else:
                    error = True
        if len(stack) > 0 and not error:
            stack.reverse()
            points.append(calc_points(list((map(lambda y: point_mapping[y], map(lambda x: mapping[x], stack))))))
        stack = []
        error = False

    points.sort()
    return points[len(points) // 2]


def split_input(puzzle):
    return puzzle.split("\n")


def main():
    puzzle = Puzzle(year=2021, day=10)
    submit(return_solution(split_input(puzzle.input_data)), part="b", day=10, year=2021)


if __name__ == '__main__':
    main()
