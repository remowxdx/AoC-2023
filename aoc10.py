#!/usr/bin/env python3
"""
Advent of Code 2023, Day 10
"""

from aoc import check_solution, save_solution, test_eq

DAY = 10


def get_input(filename):
    with open(filename, "r", encoding="ascii") as input_file:
        lines = input_file.read()
    return lines.splitlines()


def cell_connections(row, col, char):
    connections = {
        ".": [],
        "|": [(-1, 0), (1, 0)],
        "-": [(0, -1), (0, 1)],
        "L": [(-1, 0), (0, 1)],
        "J": [(-1, 0), (0, -1)],
        "7": [(0, -1), (1, 0)],
        "F": [(0, 1), (1, 0)],
        "S": [],
    }
    return [
        (row + connection[0], col + connection[1]) for connection in connections[char]
    ]


def fill_start(grid):
    start = grid["S"]
    for direction in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        cell = (start[0] + direction[0], start[1] + direction[1])
        if cell in grid and start in grid[cell]:
            grid[start].append(cell)


def parse_grid(data):
    grid = {}
    for row, line in enumerate(data):
        for col, char in enumerate(line):
            if char == "S":
                grid["S"] = (row, col)
            grid[(row, col)] = cell_connections(row, col, char)
    fill_start(grid)
    return grid


def next_cell(cell, prev, grid):
    for candidate in grid[cell]:
        if candidate != prev:
            return candidate, cell
    return None


def follow_pipes(grid):
    # print(0, grid["S"])
    prev1 = grid["S"]
    prev2 = grid["S"]
    side1 = grid[grid["S"]][0]
    side2 = grid[grid["S"]][1]
    count = 1
    while side1 != side2:
        # print(count, side1, side2)
        side1, prev1 = next_cell(side1, prev1, grid)
        side2, prev2 = next_cell(side2, prev2, grid)
        count += 1
    # print(count, side1)
    return count


def part1(data):
    grid = parse_grid(data)
    return follow_pipes(grid)


def part2(data):
    return None


def run_tests():
    test_input_1 = get_input(f"examples/ex{DAY}.1")
    test_input_2 = get_input(f"examples/ex{DAY}.2")
    print("Test Part 1:")
    test_eq("Test 1.1", part1, 4, test_input_1)
    test_eq("Test 1.2", part1, 8, test_input_2)
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
