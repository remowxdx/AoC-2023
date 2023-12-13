#!/usr/bin/env python3
"""
Advent of Code 2023, Day 13
"""

from aoc import check_solution, save_solution, test_eq

DAY = 13


def get_input(filename):
    with open(filename, "r", encoding="ascii") as input_file:
        lines = input_file.read()
    return lines.splitlines()


def parse_patterns(data):
    patterns = []
    empty = []
    pattern = empty[:]
    for line in data:
        if line == "":
            patterns.append(pattern)
            pattern = empty[:]
            continue
        pattern.append(line)
    patterns.append(pattern)
    return patterns


def find_mirror_row(pattern):
    length = len(pattern)
    # print(length)
    for num, row in enumerate(pattern[:-1]):
        to_check = min(num + 1, length - num - 1)
        mirrored = 0
        for check in range(to_check):
            # print(f"test {num - mirrored}, {num + 1 + mirrored}")
            if pattern[num - check] == pattern[num + 1 + check]:
                mirrored += 1
        if mirrored == to_check:
            return num + 1
    return 0


def is_smudged(line1, line2):
    count = 0
    for a, b in zip(line1, line2):
        if a != b:
            count += 1
    if count == 1:
        # print(line1, line2)
        return True
    return False


def find_smudged_mirror_row(pattern):
    length = len(pattern)
    # print(length)
    for num, row in enumerate(pattern[:-1]):
        to_check = min(num + 1, length - num - 1)
        smudged = 0
        mirrored = 0
        for check in range(to_check):
            # print(f"test {num - mirrored}, {num + 1 + mirrored}")
            if pattern[num - check] == pattern[num + 1 + check]:
                mirrored += 1
            elif is_smudged(pattern[num - check], pattern[num + 1 + check]):
                smudged += 1
        if mirrored == to_check - 1 and smudged == 1:
            return num + 1
    return 0


def transpose(pattern):
    transposed = []
    for row, line in enumerate(pattern):
        for col, char in enumerate(line):
            if len(transposed) <= col:
                transposed.append("")
            transposed[col] += char
    # print(transposed)
    return transposed


def part1(data):
    patterns = parse_patterns(data)
    total = 0
    for pattern in patterns:
        row = find_mirror_row(pattern)
        if row == 0:
            col = find_mirror_row(transpose(pattern))
            total += col
        total += 100 * row
    return total


def part2(data):
    patterns = parse_patterns(data)
    total = 0
    for pattern in patterns:
        row = find_smudged_mirror_row(pattern)
        if row == 0:
            col = find_smudged_mirror_row(transpose(pattern))
            total += col
        else:
            total += 100 * row
    return total


def run_tests():
    test_input_1 = get_input(f"examples/ex{DAY}")
    print("Test Part 1:")
    test_eq("Test 1.1", part1, 405, test_input_1)
    print()

    print("Test Part 2:")
    test_eq("Test 2.1", part2, 400, test_input_1)
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
