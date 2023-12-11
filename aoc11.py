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


def parse_universe(data):
    universe = set()
    for row, line in enumerate(data):
        for col, char in enumerate(line):
            if char == "#":
                universe.add((row, col))
    return len(data), len(data[0]), universe


def expand_universe(universe, age):
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
            count += age - 1

    shift_cols = {}
    count = 0
    for col in range(width):
        shift_cols[col] = col + count
        if col not in occupied_cols:
            count += age - 1

    expanded_universe = set()
    for row, col in galaxies:
        expanded_universe.add((shift_rows[row], shift_cols[col]))
    return shift_rows[height - 1] + 1, shift_cols[width - 1] + 1, expanded_universe


def min_path(from_, to_):
    return abs(from_[0] - to_[0]) + abs(from_[1] - to_[1])


def sum_paths(universe):
    _, _, galaxies = universe
    paths = 0
    for from_ in galaxies:
        for to_ in galaxies:
            paths += min_path(from_, to_)
    return paths // 2


def part1(data):
    universe = parse_universe(data)
    universe = expand_universe(universe, 2)
    lens = sum_paths(universe)
    return lens


def part2(data):
    universe = parse_universe(data)
    universe = expand_universe(universe, 1_000_000)
    lens = sum_paths(universe)
    return lens


def param_part2(age):
    def part2_aged(data):
        universe = parse_universe(data)
        universe = expand_universe(universe, age)
        lens = sum_paths(universe)
        return lens

    return part2_aged


def run_tests():
    test_input_1 = get_input(f"examples/ex{DAY}")
    print("Test Part 1:")
    test_eq("Test 1.1", part1, 374, test_input_1)
    print()

    print("Test Part 2:")
    test_eq("Test 2.1", param_part2(10), 1030, test_input_1)
    test_eq("Test 2.1", param_part2(100), 8410, test_input_1)
    test_eq("Test 2.1", param_part2(1_000_000), 82000210, test_input_1)
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
