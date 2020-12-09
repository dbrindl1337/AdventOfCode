from aocd.models import Puzzle
from aocd import submit
import networkx as nx

year = 2020
day = 7
part = "a"

bag_graph = nx.DiGraph()


def get_bag_name(bag):
    if bag[-1] == "s":
        return bag[2:][:-1]
    elif bag[0].isnumeric():
        return bag[2:]
    else:
        return bag


def build_bag_graph(bag_list):
    for bag in bag_list:
        container, containees = bag.split("s contain ")
        containees = containees.split(", ")
        container = get_bag_name(container)
        bag_graph.add_node(container)
        for containee in containees:
            if containee == "no other bags":
                continue
            num = int(containee[0])
            containee = get_bag_name(containee)
            bag_graph.add_node(containee)
            bag_graph.add_edge(container, containee, weight=num)


def return_solution(input_data):
    build_bag_graph([bags[:-1] for bags in input_data.split("\n")])
    return len(nx.ancestors(bag_graph, "shiny gold bag"))


def main():
    puzzle = Puzzle(year=year, day=day)
    submit(return_solution(puzzle.input_data), part=part, day=day, year=year)


if __name__ == '__main__':
    main()
