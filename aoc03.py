#!/usr/bin/env python3
"""
Advent of Code 2023, Day 3
"""

from aoc import check_solution, save_solution, test_eq

DAY = 3


def get_input(filename):
    with open(filename, "r", encoding="ascii") as input_file:
        lines = input_file.read()
    return lines.splitlines()


def is_symbol(char):
    if char.isdigit():
        return False
    if char == ".":
        return False
    return True


def is_gear(char):
    if char == "*":
        return True
    return False


def gear_ratio(data, row, col):
    adjacent_numbers = set()
    for x, y in [
        (row - 1, col - 1),
        (row - 1, col),
        (row - 1, col + 1),
        (row, col - 1),
        (row, col + 1),
        (row + 1, col - 1),
        (row + 1, col),
        (row + 1, col + 1),
    ]:
        if x >= 0 and x < len(data) and y >= 0 and y < len(data[x]):
            if data[x][y].isdigit():
                while data[x][y].isdigit():
                    y -= 1
                adjacent_numbers.add((x, y + 1))
    if len(adjacent_numbers) != 2:
        return 0
    product = 1
    for x, y in adjacent_numbers:
        product *= get_number(data, x, y)
    print("Ratio:", product)
    return product


def find_adjacent_numbers(data, row, col):
    adjacent_numbers = set()
    for x, y in [
        (row - 1, col - 1),
        (row - 1, col),
        (row - 1, col + 1),
        (row, col - 1),
        (row, col + 1),
        (row + 1, col - 1),
        (row + 1, col),
        (row + 1, col + 1),
    ]:
        if x >= 0 and x < len(data) and y >= 0 and y < len(data[x]):
            if data[x][y].isdigit():
                while data[x][y].isdigit():
                    y -= 1
                adjacent_numbers.add((x, y + 1))
    return adjacent_numbers


def get_number(data, x, y):
    num = 0
    while y < len(data[x]) and data[x][y].isdigit():
        num = num * 10 + int(data[x][y])
        y += 1
    # print(f"Number at ({x},{y}) is {num}.")
    return num


def sum_part_numbers(data, part_numbers):
    # print(f"Sum: {len(part_numbers)}")
    total = 0
    for x, y in part_numbers:
        total += get_number(data, x, y)
    return total


def part1(data):
    part_numbers = set()
    for row, line in enumerate(data):
        for col, char in enumerate(line):
            if is_symbol(char):
                part_numbers.update(find_adjacent_numbers(data, row, col))
    sum_parts = sum_part_numbers(data, part_numbers)
    return sum_parts


def part2(data):
    gear_ratio_sum = 0
    for row, line in enumerate(data):
        for col, char in enumerate(line):
            if is_gear(char):
                gear_ratio_sum += gear_ratio(data, row, col)
    return gear_ratio_sum


def run_tests():
    test_input_1 = get_input(f"ex{DAY}")
    print("Test Part 1:")
    test_eq("Test 1.1", part1, 4361, test_input_1)
    print()

    print("Test Part 2:")
    test_eq("Test 2.1", part2, 467835, test_input_1)
    print()


def run_part1(solved):
    data = get_input(f"input{DAY}")

    result1 = part1(data)
    print("Part 1:", result1)
    if solved:
        check_solution(DAY, 1, result1)
    else:
        save_solution(DAY, 1, result1)


def run_part2(solved):
    data = get_input(f"input{DAY}")

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
