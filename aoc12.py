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
        checks = tuple([int(check) for check in check_str.split(",")])
        records.append((record, checks))
    return records


def parse_records_5(data):
    records = []
    for line in data:
        record, check_str = line.split()
        checks = tuple([int(check) for check in check_str.split(",")] * 5)
        records.append(("?".join([record] * 5), checks))
    return records


def add(counted, new):
    """Add new cases to count."""
    for nn_check, count in new.items():
        if nn_check in counted:
            counted[nn_check] += count
        else:
            counted[nn_check] = count


CACHE = {}


def count_chunk(chunk, check, is_last=False):
    """Count ways to do the chunk."""
    global CACHE
    if (chunk, check) in CACHE:
        return CACHE[(chunk, check)]

    if chunk == "":
        return {check: 1}

    # print(chunk, check)
    if len(check) == 0:
        for char in chunk:
            if char == "#":
                return {}
        return {(): 1}

    if len(chunk) < check[0]:
        for char in chunk:
            if char == "#":
                return {}
        return {check: 1}

    if is_last:
        if len(chunk) < sum(check) + len(check) - 1:
            return {}

    res = {}

    if len(chunk) > check[0]:
        if chunk[check[0]] == "?":
            new_count = count_chunk(chunk[check[0] + 1 :], check[1:])
            add(res, new_count)
    else:
        new_count = count_chunk(chunk[check[0] + 1 :], check[1:])
        add(res, new_count)

    if chunk[0] == "?":
        new_count = count_chunk(chunk[1:], check)
        add(res, new_count)

    CACHE[(chunk, check)] = res

    return res


def count_pieces(pieces, check):
    if len(pieces) == 0:
        if len(check) == 0:
            return 1
        return 0
    total = 0
    for rest_check, ways in count_chunk(pieces[0], check).items():
        if (
            sum([len(piece) + 1 for piece in pieces[1:]])
            < sum(rest_check) + len(rest_check) - 1
        ):
            continue
        total += ways * count_pieces(pieces[1:], rest_check)
    return total


def count_ways(record):
    global CACHE
    CACHE = {}
    sequence, check = record
    pieces = sequence.split(".")
    return count_pieces(pieces, check)


def part1(data):
    records = parse_records(data)
    total_ways = 0
    for record in records:
        ways = count_ways(record)
        total_ways += ways
    return total_ways


def part2(data):
    records = parse_records_5(data)
    total_ways = 0
    for num, record in enumerate(records):
        print(num, record, end=" -> ", flush=True)
        ways = count_ways(record)
        print(ways)
        total_ways += ways
    return total_ways


def run_tests():
    test_input_1 = get_input(f"examples/ex{DAY}")
    print("Test Part 1:")
    test_eq("Test 1.1", part1, 21, test_input_1)
    print()

    print("Test Part 2:")
    test_eq("Test 2.1", part2, 525152, test_input_1)
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
