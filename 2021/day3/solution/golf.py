from aocd.models import Puzzle
from aocd import submit


def c(d, s, f):
    while len(s) > 1 and (d := d - 1):
        s = list(filter(lambda x: (x >> (d - 1)) % 2 == (1 if f(sum([((2 ** (d - 1) & r) >> (d - 1)) for r in s]), len(s) / 2) else 0), s))
    return s[0]


p = [int(i, 2) for i in Puzzle(2021, 3).input_data.split("\n")]
e = len("{0:b}".format(max(p)))
# submit(c(e + 1, p, lambda x, y: x >= y) * c(e + 1, p, lambda x, y: x < y), "b", 3, 2021)
print(c(e + 1, p, lambda x, y: x >= y) * c(e + 1, p, lambda x, y: x < y))