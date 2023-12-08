import re

from aocd.models import Puzzle
from aocd import submit


def calc_ranges(mapping):
    return range(int(mapping[0]), int(mapping[0]) + int(mapping[2])), range(int(mapping[1]),
                                                                            int(mapping[1]) + int(mapping[2]))


def calc_input_seed_ranges(mappings):
    return 0

def return_solution(seeds, mappings):
    seed_location_map = {}

    for i in range(0, len(seeds)//2 + 1, 2):
        for seed in range(seeds[i], seeds[i] + seeds[i + 1]):
            if seed in seed_location_map:
                break
            location = seed
            for mapping in mappings:
                for map in mapping:
                    if location in map[1]:
                        location = location - map[1].start + map[0].start
                        break
            seed_location_map[seed] = location

    return min(seed_location_map.values())


def split_input(puzzle):
    lines = re.split(r'\n\n[a-z-: \n]+', puzzle)

    seeds = [int(seed) for seed in re.sub(r'\w+: ', "", lines[0]).split(" ")]

    mappings = [[calc_ranges(mapping.split(" ")) for mapping in line.split("\n")] for line in lines[1:]]

    return seeds, mappings


def main():
    puzzle = Puzzle(year=2023, day=5)
    submit(return_solution(split_input(puzzle.input_data)), part="b", day=5, year=2023)


if __name__ == '__main__':
    main()
