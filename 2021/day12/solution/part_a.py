from aocd.models import Puzzle
from aocd import submit

import networkx as nx

paths = []


def traverse(graph, start, end, path, already_visited):
    if start == end:
        path.append(end)
        paths.append(path)
        return
    path.append(start)
    for neighbor in nx.Graph.neighbors(graph, start):
        if neighbor in already_visited:
            continue
        traverse(graph, neighbor, end, path[:], already_visited + [neighbor] if neighbor.islower() else already_visited[:])


def return_solution(graph):
    traverse(graph, "start", "end", [], ["start"])
    return len(paths)


def split_input(puzzle):
    lines = puzzle.split("\n")

    nodes = [node.split("-") for node in lines]

    graph = nx.Graph()

    graph.add_edges_from(nodes)

    return graph


def main():
    puzzle = Puzzle(year=2021, day=12)
    submit(return_solution(split_input(puzzle.input_data)), part="a", day=12, year=2021)


if __name__ == '__main__':
    main()
