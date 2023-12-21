#!/usr/bin/env python3
"""
Advent of Code 2023, Day 21
"""

from aoc import check_solution, save_solution, test_eq

DAY = 21


def get_input(filename):
    with open(filename, "r", encoding="ascii") as input_file:
        lines = input_file.read()
    return lines.splitlines()


def parse_map(data):
    grid = {}
    for row, line in enumerate(data):
        for col, char in enumerate(line):
            if char == ".":
                grid[(row, col)] = -1
            elif char == "S":
                grid[(row, col)] = 0
                grid["S"] = (row, col)
    return grid


def set_neighbours(grid, positions, step):
    for pos in positions:
        neigh = (pos[0] - 1, pos[1])
        if neigh in grid:
            grid[neigh] = step
        neigh = (pos[0], pos[1] - 1)
        if neigh in grid:
            grid[neigh] = step
        neigh = (pos[0] + 1, pos[1])
        if neigh in grid:
            grid[neigh] = step
        neigh = (pos[0], pos[1] + 1)
        if neigh in grid:
            grid[neigh] = step


def reachable(grid, steps):
    for step in range(steps):
        reachables = []
        for pos in grid:
            if grid[pos] == step:
                reachables.append(pos)
        set_neighbours(grid, reachables, step + 1)
    count = 0
    for step in grid.values():
        if step == steps:
            count += 1
    return count


def part1(data, steps):
    grid = parse_map(data)
    count = reachable(grid, steps)
    return count


def part2(data, steps):
    return None


def run_tests():
    test_input_1 = get_input(f"examples/ex{DAY}")
    print("Test Part 1:")
    test_eq("Test 1.1", part1, 16, test_input_1, 6)
    print()

    print("Test Part 2:")
    test_eq("Test 2.1", part2, 42, test_input_1)
    print()


def run_part1(solved):
    data = get_input(f"inputs/input{DAY}")

    result1 = part1(data, 64)
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
