import shutil
import datetime
import pyperclip
import os


now = datetime.datetime.now()
year = now.year

get_solution = "puzzle"
get_solution_split_by_lines = f"{get_solution}.split(\"\\n\")"
get_solution_split_by_lines_into_tuples = f"[i.split() for i in {get_solution_split_by_lines}]"

windows_style_newline = "\r\n"
unix_style_newline = "\n"

# manually override these:
day = now.day
preprocess_solution_str = get_solution_split_by_lines

src = 'day_template'
dest = f'../{year}/day{day}'


def get_solution_template(part, prepocess_solution):
    return f"""from aocd.models import Puzzle
from aocd import submit


def return_solution(lines):
    pass


def split_input(puzzle):
    lines = {prepocess_solution}
    return lines


def main():
    puzzle = Puzzle(year={year}, day={day})
    submit(return_solution(split_input(puzzle.input_data)), part="{part}", day={day}, year={year})


if __name__ == '__main__':
    main()
"""


def get_test_template():
    return f"""from ..solution import part_a as a
from ..solution import part_b as b

input_a = \"\"\"{pyperclip.paste().replace(windows_style_newline, unix_style_newline)}\"\"\"

input_b = input_a  # replace me


def test_correct_example_solution_part_a():
    assert a.return_solution(a.split_input(input_a)) == 0  # replace me


def test_correct_example_solution_part_b():
    assert b.return_solution(b.split_input(input_b)) == 0  # replace me
"""


def populate_solution_template(part):
    f = open(f"{dest}/solution/part_{part}.py", "w")
    f.write(get_solution_template(part, preprocess_solution_str))
    f.close()


def populate_test_template():
    f = open(f"{dest}/tests/tests.py", "w")
    f.write(get_test_template())
    f.close()
    os.rename(f"{dest}/tests/tests.py", f"{dest}/tests/tests_day{day}_{year}.py")


def main():
    shutil.copytree(src, dest)
    for file in ["a", "b"]:
        populate_solution_template(file)
    populate_test_template()


if __name__ == '__main__':
    main()


