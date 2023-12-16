#!/usr/bin/env python3
"""
Advent of Code 2023, Day 16
"""

from aoc import check_solution, save_solution, test_eq

DAY = 16


def get_input(filename):
    with open(filename, "r", encoding="ascii") as input_file:
        lines = input_file.read()
    return lines.splitlines()


def parse_contraption(data):
    contraption = {"s": (len(data), len(data[0]))}
    for row, line in enumerate(data):
        for col, char in enumerate(line):
            if char != ".":
                contraption[(row, col)] = {"t": char}
    return contraption


def next_pos(pos, direction):
    row, col = pos
    if direction == ">":
        return (row, col + 1, direction)
    if direction == "<":
        return (row, col - 1, direction)
    if direction == "^":
        return (row - 1, col, direction)
    if direction == "v":
        return (row + 1, col, direction)
    raise ValueError("Unknown direction")


def reflect(beam, typ):
    next_dir = {
        ">-": [(0, 1, ">")],
        ">|": [(1, 0, "v"), (-1, 0, "^")],
        ">\\": [(1, 0, "v")],
        ">/": [(-1, 0, "^")],
        "<-": [(0, -1, "<")],
        "<|": [(1, 0, "v"), (-1, 0, "^")],
        "<\\": [(-1, 0, "^")],
        "</": [(1, 0, "v")],
        "^-": [(0, 1, ">"), (0, -1, "<")],
        "^|": [(-1, 0, "^")],
        "^\\": [(0, -1, "<")],
        "^/": [(0, 1, ">")],
        "v-": [(0, 1, ">"), (0, -1, "<")],
        "v|": [(1, 0, "v")],
        "v\\": [(0, 1, ">")],
        "v/": [(0, -1, "<")],
    }

    return [
        (beam[0] + n_d[0], beam[1] + n_d[1], n_d[2]) for n_d in next_dir[beam[2] + typ]
    ]


def shoot_beam(beam, contr):
    beams = [beam]
    height, width = contr["s"]
    count = 0
    while len(beams) > 0:
        beam = beams.pop()
        pos = (beam[0], beam[1])

        if pos[0] < 0 or pos[1] < 0:
            continue
        if pos[0] >= height or pos[1] >= width:
            continue

        if pos in contr:
            if "b" in contr[pos]:
                if beam[2] not in contr[pos]["b"]:
                    contr[pos]["b"].append(beam[2])
                else:
                    continue
            else:
                contr[pos]["b"] = [beam[2]]
                count += 1
        else:
            contr[pos] = {"b": [beam[2]]}
            count += 1

        if "t" not in contr[pos]:
            beams.append(next_pos(pos, beam[2]))
        else:
            typ = contr[pos]["t"]
            for next_beam in reflect(beam, typ):
                beams.append(next_beam)
    return count


def count_energized(contr):
    count = 0
    for pos in contr:
        if pos == "s":
            continue
        if "b" in contr[pos]:
            count += 1
    return count


def part1(data):
    contr = parse_contraption(data)
    _ = shoot_beam((0, 0, ">"), contr)
    ener = count_energized(contr)
    return ener


def part2(data):
    contr = parse_contraption(data)
    max_ener = 0
    height, width = contr["s"]
    for row in range(height):
        c = parse_contraption(data)
        count = shoot_beam((row, 0, ">"), c)
        max_ener = max(max_ener, count)
        c = parse_contraption(data)
        count = shoot_beam((row, width - 1, "<"), c)
        max_ener = max(max_ener, count)
    for col in range(width):
        c = parse_contraption(data)
        count = shoot_beam((0, col, "v"), c)
        max_ener = max(max_ener, count)
        c = parse_contraption(data)
        count = shoot_beam((height - 1, col, "^"), c)
        max_ener = max(max_ener, count)
    return max_ener


def run_tests():
    test_input_1 = get_input(f"examples/ex{DAY}")
    print("Test Part 1:")
    test_eq("Test 1.1", part1, 46, test_input_1)
    print()

    print("Test Part 2:")
    test_eq("Test 2.1", part2, 51, test_input_1)
    print()


def run_part1(solved):
    data = get_input(f"inputs/input{DAY}")

    result1 = part1(data)
    print("Part 1:", result1)
    if solved:
        check_solution(DAY, 1, result1)
    else:
        save_solution(DAY, 1, result1)


def run_part2(solved):
    data = get_input(f"inputs/input{DAY}")

    result2 = part2(data)
    print("Part 2:", result2)
    if solved:
        check_solution(DAY, 2, result2)
    else:
        save_solution(DAY, 2, result2)


def main():
    run_tests()
    run_part1(True)
    run_part2(True)


if __name__ == "__main__":
    main()
