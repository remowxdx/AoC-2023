#!/usr/bin/env python3
"""
Advent of Code 2023, Day 15
"""

from aoc import check_solution, save_solution, test_eq

DAY = 15


def get_input(filename):
    with open(filename, "r", encoding="ascii") as input_file:
        lines = input_file.read()
    return lines.splitlines()


def parse_init(data):
    sequence = []
    for line in data:
        for step in line.split(","):
            sequence.append(step)
    return sequence


def hash(string):
    value = 0
    for char in string:
        value += ord(char)
        value *= 17
        value %= 256
    return value


def part1(data):
    sequence = parse_init(data)
    return sum([hash(step) for step in sequence])


def focusing_power(boxes):
    power = 0
    for num, box in enumerate(boxes):
        slot = 1
        for lens, focus in box.items():
            power += (num + 1) * slot * focus
            slot += 1
    return power


def part2(data):
    sequence = parse_init(data)
    boxes = [dict() for _ in range(256)]
    for step in sequence:
        if step[-1] == "-":
            label = step[:-1]
            box = hash(label)
            if label in boxes[box]:
                del boxes[box][label]
        else:
            label, focus_str = step.split("=")
            focus = int(focus_str)
            box = hash(label)
            boxes[box][label] = focus

    # print("\n".join([str(box) for box in boxes if box]))
    return focusing_power(boxes)


def run_tests():
    test_input_1 = get_input(f"examples/ex{DAY}")
    print("Test Part 1:")
    test_eq("Test 1.1", part1, 1320, test_input_1)
    print()

    print("Test Part 2:")
    test_eq("Test 2.1", part2, 145, test_input_1)
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
