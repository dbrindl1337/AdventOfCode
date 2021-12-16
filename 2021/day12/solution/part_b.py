from aocd.models import Puzzle
from aocd import submit

import networkx as nx

paths = set()


def traverse(graph, start, end, path, already_visited, twice):
    if start == end:
        path.append(end)
        paths.add(tuple(path))
        return
    path.append(start)
    for neighbor in nx.Graph.neighbors(graph, start):
        if neighbor in already_visited:
            continue
        traverse(graph, neighbor, end, path[:], already_visited + [neighbor] if (neighbor.islower() and twice != neighbor) else already_visited[:], twice if twice != neighbor else '')


def return_solution(graph):
    small_caves = list(filter(lambda x: x.islower() and x != "start" and x != "end", graph.nodes))
    for cave in small_caves:
        traverse(graph, "start", "end", [], ["start"], cave)
    return len(paths)


def split_input(puzzle):
    lines = puzzle.split("\n")

    nodes = [node.split("-") for node in lines]

    graph = nx.Graph()

    graph.add_edges_from(nodes)

    return graph


def main():
    puzzle = Puzzle(year=2021, day=12)
    submit(return_solution(split_input(puzzle.input_data)), part="b", day=12, year=2021)


if __name__ == '__main__':
    main()
