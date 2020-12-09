from aocd.models import Puzzle
from aocd import submit

year = 2020
day = 8
part = "b"

cmd = 0
cmd_arg = 1
not_yet_executed = 2

instruction_pointer = 0
accumulator = 0


def nop(cnt):
    global instruction_pointer
    instruction_pointer += 1
    return cnt


def acc(number):
    global accumulator
    global instruction_pointer
    instruction_pointer += 1
    accumulator += number


def jmp(offset):
    global instruction_pointer
    instruction_pointer += offset


instruction_map = {
    "nop": nop,
    "acc": acc,
    "jmp": jmp
}


def map_commands(line):
    command, arg = line.split(" ")
    return [instruction_map[command], int(arg), True]


def execute(program):
    while program[instruction_pointer][not_yet_executed]:
        program[instruction_pointer][not_yet_executed] = False
        program[instruction_pointer][cmd](program[instruction_pointer][cmd_arg])
        if instruction_pointer >= len(program):
            return accumulator

    return -1


def return_solution(input_data):
    global instruction_pointer, accumulator
    program = list(map(map_commands, input_data.split("\n")))

    for line_cnt in range(0, len(program)):
        reset(program)
        if program[line_cnt][cmd] == nop:
            program[line_cnt][cmd] = jmp
            if execute(program) == -1:
                program[line_cnt][cmd] = nop
                continue
            else:
                return accumulator
        elif program[line_cnt][cmd] == jmp:
            program[line_cnt][cmd] = nop
            if execute(program) == -1:
                program[line_cnt][cmd] = jmp
                continue
            else:
                return accumulator


def reset(program):
    global instruction_pointer, accumulator
    instruction_pointer = 0
    accumulator = 0
    for line in program:
        line[not_yet_executed] = True


def main():
    puzzle = Puzzle(year=year, day=day)
    submit(return_solution(puzzle.input_data), part=part, day=day, year=year)


if __name__ == '__main__':
    main()
