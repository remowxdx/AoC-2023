#!/usr/bin/env python3
"""
Advent of Code 2023, Day 18
"""

from aoc import check_solution, save_solution, test_eq

DAY = 18


def get_input(filename):
    with open(filename, "r", encoding="ascii") as input_file:
        lines = input_file.read()
    return lines.splitlines()


def parse_plan(data):
    grid = {}
    pos = [0, 0]
    max_pos = [0, 0]
    min_pos = [0, 0]
    for line in data:
        direction, steps, color = line.split()
        for _ in range(int(steps)):
            if direction == "R":
                pos[1] += 1
            elif direction == "L":
                pos[1] -= 1
            elif direction == "D":
                pos[0] += 1
            elif direction == "U":
                pos[0] -= 1
            max_pos[0] = max(max_pos[0], pos[0])
            max_pos[1] = max(max_pos[1], pos[1])
            min_pos[0] = min(min_pos[0], pos[0])
            min_pos[1] = min(min_pos[1], pos[1])
            grid[tuple(pos)] = color[1:-1]
    return grid, min_pos[0] - 1, min_pos[1] - 1, max_pos[0] + 2, max_pos[1] + 2


def neighbours(pos):
    return [
        (pos[0] + 1, pos[1]),
        (pos[0], pos[1] + 1),
        (pos[0] - 1, pos[1]),
        (pos[0], pos[1] - 1),
    ]


def exterior(grid, top, left, bottom, right):
    to_visit = [(top, left)]
    visited = set()
    while len(to_visit) > 0:
        pos = to_visit.pop()
        if pos in visited:
            continue
        if pos in grid:
            continue
        if pos[0] < top or pos[1] < left:
            continue
        if pos[0] >= bottom or pos[1] >= right:
            continue
        visited.add(pos)
        to_visit.extend(neighbours(pos))
    return visited


def part1(data):
    grid, top, left, bottom, right = parse_plan(data)
    # print(grid, top, left, bottom, right)
    external = exterior(grid, top, left, bottom, right)
    # print(external)
    return (bottom - top) * (right - left) - len(external)


def part2(data):
    return None


def run_tests():
    test_input_1 = get_input(f"examples/ex{DAY}")
    print("Test Part 1:")
    test_eq("Test 1.1", part1, 62, test_input_1)
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
