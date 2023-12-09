#!/usr/bin/env python3
"""
Advent of Code 2023, Day 1
"""

from aoc import check_solution, save_solution, test_eq

DAY = 1

DIGITS = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def get_input(filename):
    with open(filename, "r", encoding="ascii") as input_file:
        lines = input_file.read()
    return lines.splitlines()


def get_first_digit(line):
    for char in line:
        if char.isdigit():
            return int(char)
    return -1


def get_last_digit(line):
    for char in reversed(line):
        if char.isdigit():
            return int(char)
    return -1


def get_digits(line):
    found = {}
    for digit, value in DIGITS.items():
        idx = line.find(digit)
        while idx >= 0:
            found[idx] = value
            idx = line.find(digit, idx + 1)
    for pos, char in enumerate(line):
        if char.isdigit():
            found[pos] = int(char)
    # print(line, found)
    return found


def first_last(found):
    first = None
    last = None
    for i in sorted(found.keys()):
        if first is None:
            first = found[i]
        last = found[i]
    return first, last


def part1(data):
    total = 0
    for line in data:
        if line == "":
            continue
        first = get_first_digit(line)
        last = get_last_digit(line)
        value = first * 10 + last
        total += value
    return total


def part2(data):
    total = 0
    for line in data:
        first, last = first_last(get_digits(line))
        total += first * 10 + last
    return total


def run_tests():
    test_input_1 = get_input(f"examples/ex{DAY}")
    print("Test Part 1:")
    test_eq("Test 1.1", part1, 142, test_input_1)
    print()

    test_input_2 = get_input(f"examples/ex{DAY}.2")
    print("Test Part 2:")
    test_eq("Test 2.1", part2, 281, test_input_2)
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
