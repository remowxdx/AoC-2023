#!/usr/bin/env python3
"""
Advent of Code 2023, Day 12
"""

from aoc import check_solution, save_solution, test_eq

DAY = 12


def get_input(filename):
    with open(filename, "r", encoding="ascii") as input_file:
        lines = input_file.read()
    return lines.splitlines()


def parse_records(data):
    records = []
    for line in data:
        record, check_str = line.split()
        checks = [int(check) for check in check_str.split(",")]
        records.append((record, checks))
    return records


def to_check(record):
    run = []
    count = 0
    for char in record:
        if char == "#":
            count += 1
        else:
            if count > 0:
                run.append(count)
                count = 0
    if count > 0:
        run.append(count)
    return run


def fitting(record, check):
    return to_check(record) == check


def count_unknown(record):
    count = 0
    for char in record:
        if char == "?":
            count += 1
    return count


def count_ways(record):
    num = count_unknown(record[0])
    ways = 0
    for way in range(2 ** num):
        cur = way
        test = ""
        for char in record[0]:
            if char == "?":
                test += "#" if cur % 2 == 0 else "."
                cur >>= 1
            else:
                test += char
        if fitting(test, record[1]):
            ways += 1
            # print("----", way, ways, test)
    return ways


def part1(data):
    records = parse_records(data)
    total_ways = 0
    for record in records:
        ways = count_ways(record)
        # print(record, ways)
        total_ways += ways
    return total_ways


def part2(data):
    return None


def run_tests():
    test_input_1 = get_input(f"examples/ex{DAY}")
    print("Test Part 1:")
    test_eq("Test 1.1", part1, 21, test_input_1)
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
