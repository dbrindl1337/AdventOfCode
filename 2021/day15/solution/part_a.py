from aocd.models import Puzzle
from aocd import submit

import networkx as nx


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

    side_length = len(lines) - 1

    graph = nx.DiGraph()

    for i, line in enumerate(lines):
        for j, chiton in enumerate(line):
            graph.add_node((i, j))

    for i, line in enumerate(lines):
        for j, chiton in enumerate(line):
            set_edges(graph, (i, j), int(chiton))

    return graph, side_length


def main():
    puzzle = Puzzle(year=2021, day=15)
    submit(return_solution(*split_input(puzzle.input_data)), part="a", day=15, year=2021)


if __name__ == '__main__':
    main()
