from aocd.models import Puzzle
from aocd import submit


def return_solution(fish, days):
    for d in range(days):
        new_fish = fish[0]
        fish[0] = fish[1]
        fish[1] = fish[2]
        fish[2] = fish[3]
        fish[3] = fish[4]
        fish[4] = fish[5]
        fish[5] = fish[6]
        fish[6] = fish[7]
        fish[7] = fish[8]
        fish[8] = new_fish
        fish[6] += new_fish
    return sum(fish)


def split_input(puzzle):
    initial = [int(i) for i in puzzle.split(",")]
    fish = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for f in initial:
        fish[f] += 1
    return fish


def main():
    puzzle = Puzzle(year=2021, day=6)
    submit(return_solution(split_input(puzzle.input_data), 256), part="b", day=6, year=2021)


if __name__ == '__main__':
    main()
