from aocd.models import Puzzle
from aocd import submit

puzzle = Puzzle(year=2021, day=7).input_data.split(",")


submit(min([sum([abs(k-i) for k in [int(i) for i in puzzle]]) for i in range(0, len(puzzle))]), part="a", day=7, year=2021)
submit(min([sum([(abs(k-i) * (abs(k-i) + 1)) // 2 for k in [int(i) for i in puzzle]]) for i in range(0, len(puzzle))]), part="b", day=7, year=2021)


