#!/usr/bin/env python3
"""
Advent of Code 2023, Day 14
"""

from aoc import check_solution, save_solution, test_eq

DAY = 14


def get_input(filename):
    with open(filename, "r", encoding="ascii") as input_file:
        lines = input_file.read()
    return lines.splitlines()


def parse_platform(data):
    platform = []
    for line in data:
        platform.append(line)
    return platform


def slide_stone(row, col, platform):
    for slide in range(row, 0, -1):
        if platform[slide - 1][col] == ".":
            platform[slide] = platform[slide][:col] + "." + platform[slide][col + 1 :]
            platform[slide - 1] = (
                platform[slide - 1][:col] + "O" + platform[slide - 1][col + 1 :]
            )
        else:
            break


def tilt_north(platform):
    for row, line in enumerate(platform):
        for col, char in enumerate(line):
            if char == "O":
                slide_stone(row, col, platform)


def calc_weight(platform):
    load = len(platform)
    weight = 0
    for line in platform:
        for char in line:
            if char == "O":
                weight += load
        load -= 1
    return weight


def part1(data):
    platform = parse_platform(data)
    tilt_north(platform)
    # print(platform)
    weight = calc_weight(platform)
    return weight


def part2(data):
    return None


def run_tests():
    test_input_1 = get_input(f"examples/ex{DAY}")
    print("Test Part 1:")
    test_eq("Test 1.1", part1, 136, test_input_1)
    print()

    print("Test Part 2:")
    test_eq("Test 2.1", part2, 64, test_input_1)
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
