#!/usr/bin/env python3
"""
Advent of Code 2023, Day 9
"""

from aoc import check_solution, save_solution, test_eq

DAY = 9


def get_input(filename):
    with open(filename, "r", encoding="ascii") as input_file:
        lines = input_file.read()
    return lines.splitlines()


def parse_sequence(line):
    return [int(value) for value in line.split()]


def differences(sequence):
    prev = sequence[0]
    diff = []
    for value in sequence[1:]:
        diff.append(value - prev)
        prev = value
    return diff


def next_value(sequence):
    for value in sequence:
        if value != 0:
            return sequence[-1] + next_value(differences(sequence))
    return 0


def prev_value(sequence):
    for value in sequence:
        if value != 0:
            return sequence[0] - prev_value(differences(sequence))
    return 0


def part1(data):
    total = 0
    for line in data:
        sequence = parse_sequence(line)
        total += next_value(sequence)
    return total


def part2(data):
    total = 0
    for line in data:
        sequence = parse_sequence(line)
        total += prev_value(sequence)
    return total


def run_tests():
    test_input_1 = get_input(f"examples/ex{DAY}")
    print("Test Part 1:")
    test_eq("Test 1.1", part1, 114, test_input_1)
    print()

    print("Test Part 2:")
    test_eq("Test 2.1", part2, 2, test_input_1)
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
