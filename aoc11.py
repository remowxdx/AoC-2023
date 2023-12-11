#!/usr/bin/env python3
"""
Advent of Code 2023, Day 11
"""

from aoc import check_solution, save_solution, test_eq

DAY = 11


def get_input(filename):
    with open(filename, "r", encoding="ascii") as input_file:
        lines = input_file.read()
    return lines.splitlines()


class Universe:
    pass


def parse_universe(data):
    universe = set()
    for row, line in enumerate(data):
        for col, char in enumerate(line):
            if char == "#":
                universe.add((row, col))
    return row + 1, col + 1, universe


def expand_universe(universe):
    height, width, galaxies = universe

    occupied_rows = set()
    occupied_cols = set()
    for row, col in galaxies:
        occupied_rows.add(row)
        occupied_cols.add(col)

    shift_rows = {}
    count = 0
    for row in range(height):
        shift_rows[row] = row + count
        if row not in occupied_rows:
            count += 1

    shift_cols = {}
    count = 0
    for col in range(width):
        shift_cols[col] = col + count
        if col not in occupied_cols:
            count += 1

    expanded_universe = set()
    for row, col in galaxies:
        expanded_universe.add((shift_rows[row], shift_cols[col]))
    return shift_rows[height - 1] + 1, shift_cols[width - 1] + 1, expanded_universe


def min_path(from_, to):
    return abs(from_[0] - to[0]) + abs(from_[1] - to[1])


def sum_paths(universe):
    _, _, galaxies = universe
    paths = 0
    for from_ in galaxies:
        for to in galaxies:
            paths += min_path(from_, to)
    return paths / 2


def part1(data):
    universe = parse_universe(data)
    universe = expand_universe(universe)
    lens = sum_paths(universe)
    return lens


def part2(data):
    return None


def run_tests():
    test_input_1 = get_input(f"examples/ex{DAY}")
    print("Test Part 1:")
    test_eq("Test 1.1", part1, 374, test_input_1)
    print()

    print("Test Part 2:")
    test_eq("Test 2.1", part2, 42, test_input_1)
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
    # run_part2(False)


if __name__ == "__main__":
    main()
