from aocd.models import Puzzle
from aocd import submit

import networkx as nx
import numpy as np


def return_solution(graph, side_length):
    return nx.shortest_path_length(graph, (0, 0), (side_length, side_length), weight="weight")


def get_kernel(x, y):
    return [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]


def set_edges(graph, target, weight):
    for source in get_kernel(*target):
        if graph.has_node(source):
            graph.add_weighted_edges_from([(source, target, weight)])


def split_input(puzzle):
    lines = puzzle.split("\n")

    base_side_length = len(lines)
    side_length = 5 * len(lines) - 1

    graph = nx.DiGraph()
    a = np.zeros((side_length + 1, side_length + 1))

    for extend_x in range(0, 5):
        for extend_y in range(0, 5):
            for i, line in enumerate(lines):
                for j, chiton in enumerate(line):
                    graph.add_node((extend_x * base_side_length + i, extend_y * base_side_length + j))
                    a[extend_x * base_side_length + i, extend_y * base_side_length + j] = ((int(chiton) + extend_x + extend_y - 1) % 9) + 1

    for extend_x in range(0, 5):
        for extend_y in range(0, 5):
            for i, line in enumerate(lines):
                for j, chiton in enumerate(line):
                    set_edges(graph, (extend_x * base_side_length + i, extend_y * base_side_length + j), ((int(chiton) + extend_x + extend_y - 1) % 9) + 1)

    return graph, side_length


def main():
    puzzle = Puzzle(year=2021, day=15)
    submit(return_solution(*split_input(puzzle.input_data)), part="b", day=15, year=2021)


if __name__ == '__main__':
    main()
