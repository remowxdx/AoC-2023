#!/usr/bin/env python3
"""
Advent of Code 2023, Day 6
"""

import math
from aoc import check_solution, save_solution, test_eq

DAY = 6


def get_input(filename):
    with open(filename, "r", encoding="ascii") as input_file:
        lines = input_file.read()
    return lines.splitlines()


def parse(data):
    times = [int(time) for time in data[0].split()[1:]]
    records = [int(record) for record in data[1].split()[1:]]
    return times, records


def parse2(data):
    time = int(data[0].split(":")[1].replace(" ", ""))
    record = int(data[1].split(":")[1].replace(" ", ""))
    return time, record


def distance(time, press):
    # v = d/t => d = v*t
    dist = press * (time - press)
    return dist


def part1(data):
    times, records = parse(data)

    counts = []
    ways = 1
    for race_number in range(len(times)):
        count = 0
        for press in range(times[race_number]):
            dist = distance(times[race_number], press)
            if dist > records[race_number]:
                count += 1
        counts.append(count)
        ways *= count

    return ways


def from_to(time, record):
    sqrt_disc = math.sqrt(time * time - 4 * record)
    # print("disc", disc)
    from_ = (time - sqrt_disc) / 2
    to = (time + sqrt_disc) / 2
    return from_, to


def part2(data):
    time, record = parse2(data)

    # print(time, record)
    f, t = from_to(time, record)
    # print(f, t)
    count = int(t) - int(f)

    return count


def run_tests():
    test_input_1 = get_input(f"examples/ex{DAY}")
    print("Test Part 1:")
    test_eq("Test 1.1", part1, 288, test_input_1)
    print()

    print("Test Part 2:")
    test_eq("Test 2.1", part2, 71503, test_input_1)
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
