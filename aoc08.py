#!/usr/bin/env python3
"""
Advent of Code 2023, Day 8
"""

from aoc import check_solution, save_solution, test_eq

DAY = 8


def get_input(filename):
    with open(filename, "r", encoding="ascii") as input_file:
        lines = input_file.read()
    return lines.splitlines()


def parse_input(data):
    instructions = data[0]

    nodes = {}
    for line in data[2:]:
        node, l_r = line.split(" = ")
        left, right = l_r.strip("()").split(", ")
        nodes[node] = (left, right)
    return instructions, nodes


def part1(data):
    instructions, nodes = parse_input(data)
    node = "AAA"
    instruction = 0
    while node != "ZZZ":
        if instructions[instruction % len(instructions)] == "L":
            node = nodes[node][0]
        else:
            node = nodes[node][1]
        instruction += 1
    return instruction


def part2(data):
    return None


def run_tests():
    test_input_1 = get_input(f"ex{DAY}.1")
    test_input_2 = get_input(f"ex{DAY}.2")
    print("Test Part 1:")
    test_eq("Test 1.1", part1, 2, test_input_1)
    test_eq("Test 1.2", part1, 6, test_input_2)
    print()

    print("Test Part 2:")
    test_eq("Test 2.1", part2, 42, test_input_1)
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
    # run_part2(False)


if __name__ == "__main__":
    main()
