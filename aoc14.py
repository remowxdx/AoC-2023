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
    height = len(data)
    width = len(data[0])
    stones = {}
    for row, line in enumerate(data):
        for col, char in enumerate(line):
            if char != ".":
                stones[(row, col)] = char
    return height, width, stones


def tilt_north(platform):
    height, width, stones = platform
    tilted_stones = {}
    for row in range(height):
        for col in range(width):
            if (row, col) in stones:
                if stones[(row, col)] == "O":
                    for slided_row in range(row - 1, -1, -1):
                        if (slided_row, col) in tilted_stones:
                            tilted_stones[(slided_row + 1, col)] = "O"
                            break
                    else:
                        tilted_stones[(0, col)] = "O"
                else:
                    tilted_stones[(row, col)] = "#"
    return height, width, tilted_stones


def tilt_west(platform):
    height, width, stones = platform
    tilted_stones = {}
    for col in range(width):
        for row in range(height):
            if (row, col) in stones:
                if stones[(row, col)] == "O":
                    for slided_col in range(col - 1, -1, -1):
                        if (row, slided_col) in tilted_stones:
                            tilted_stones[(row, slided_col + 1)] = "O"
                            break
                    else:
                        tilted_stones[(row, 0)] = "O"
                else:
                    tilted_stones[(row, col)] = "#"
    return height, width, tilted_stones


def tilt_south(platform):
    height, width, stones = platform
    tilted_stones = {}
    for row in range(height - 1, -1, -1):
        for col in range(width):
            if (row, col) in stones:
                if stones[(row, col)] == "O":
                    for slided_row in range(row + 1, height):
                        if (slided_row, col) in tilted_stones:
                            tilted_stones[(slided_row - 1, col)] = "O"
                            break
                    else:
                        tilted_stones[(height - 1, col)] = "O"
                else:
                    tilted_stones[(row, col)] = "#"
    return height, width, tilted_stones


def tilt_east(platform):
    height, width, stones = platform
    tilted_stones = {}
    for col in range(width - 1, -1, -1):
        for row in range(height):
            if (row, col) in stones:
                if stones[(row, col)] == "O":
                    for slided_col in range(col + 1, width):
                        if (row, slided_col) in tilted_stones:
                            tilted_stones[(row, slided_col - 1)] = "O"
                            break
                    else:
                        tilted_stones[(row, width - 1)] = "O"
                else:
                    tilted_stones[(row, col)] = "#"
    return height, width, tilted_stones


def calc_weight(platform):
    height, _, stones = platform
    weight = 0
    for pos in stones:
        if stones[pos] == "O":
            weight += height - pos[0]
    return weight


def print_platform(platform):
    height, width, stones = platform
    for row in range(height):
        for col in range(width):
            if (row, col) in stones:
                print(stones[(row, col)], end="")
            else:
                print(".", end="")
        print()


def part1(data):
    # print()
    platform = parse_platform(data)
    # print_platform(platform)
    # print()
    tp = tilt_north(platform)
    # print_platform(tp)
    weight = calc_weight(tp)
    return weight


def cycle_platform(platform):
    return tilt_east(tilt_south(tilt_west(tilt_north(platform))))


def part2(data):
    # print()
    platform = parse_platform(data)
    # print()
    # print_platform(platform)
    weights = []
    stones = []
    for cycle in range(1000000000):
        platform = cycle_platform(platform)
        for idx in range(len(stones) - 1, -1, -1):
            if stones[idx] == platform[2]:
                # print(f"Cycle from {idx} to {cycle}.")
                # print(weights)
                return weights[idx + (1000000000 - idx - 1) % (cycle - idx)]
        stones.append(platform[2])
        # print_platform(platform)
        # print()
        weights.append(calc_weight(platform))
    # print(weights)
    return weights[-1]


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
    run_part2(True)


if __name__ == "__main__":
    main()
