def split_by_lines(puzzle_input):
    return puzzle_input.split("\n")


def split_by_lines_in_tuples(puzzle_input):
    [i.split() for i in split_by_lines(puzzle_input)]
