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
        if char == "?":
            if count > 0:
                run.append(count)
            return run
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
    for char in record:
        if char == "?":
            raise ValueError
    return to_check(record) == check


def count_unknown(record):
    count = 0
    for char in record:
        if char == "?":
            count += 1
    return count


def get_unknowns(record):
    unknowns = []
    for pos, char in enumerate(record):
        if char == "?":
            unknowns.append(pos)
    return unknowns


def get_damaged(record):
    damaged = []
    for pos, char in enumerate(record):
        if char == "#":
            damaged.append(pos)
    return damaged


def part_fitting(part, check):
    if len(part) == 0:
        return True
    if len(part) > len(check):
        return False
    for pos, length in enumerate(part[:-1]):
        if length != check[pos]:
            return False
    pos = len(part) - 1
    # print(pos, part, check)
    if part[pos] > check[pos]:
        return False
    return True


def fill_next(state, record, unknowns, check):
    pos = unknowns[0]
    next_unknowns = unknowns[1:]
    next_record = record[:pos] + state + record[pos + 1 :]
    if len(next_unknowns) == 0:
        if fitting(next_record, check):
            return 1
        return 0
    if not part_fitting(to_check(next_record), check):
        # print(next_record, to_check(next_record), check)
        return 0
    result = fill_next("#", next_record, next_unknowns, check) + fill_next(
        ".", next_record, next_unknowns, check
    )
    return result


def count_ways(record):
    unknowns = get_unknowns(record[0])
    return fill_next(".", record[0], unknowns, record[1]) + fill_next(
        "#", record[0], unknowns, record[1]
    )


def part1(data):
    records = parse_records(data)
    total_ways = 0
    for record in records:
        ways = count_ways(record)
        print(record, ways)
        total_ways += ways
    return total_ways


def part2(data):
    f_records = parse_records(data)
    count = 1
    total_ways = 0
    for f_record in f_records:
        record = ("?".join([f_record[0]] * 5), f_record[1] * 5)
        f_ways = count_ways(f_record)
        ff_ways = count_ways(("#".join([f_record[0]] * 2), f_record[1] * 2))
        fff_ways = count_ways(("#".join([f_record[0]] * 3), f_record[1] * 3))
        ffff_ways = count_ways(("#".join([f_record[0]] * 4), f_record[1] * 4))
        fffff_ways = count_ways(("#".join([f_record[0]] * 5), f_record[1] * 5))
        print(f_ways, ff_ways, fff_ways, ffff_ways, fffff_ways)
        ways = f_ways ** 5
        ways += (ff_ways ** 2 * f_ways) * 3
        ways += (ff_ways * f_ways ** 3) * 4
        ways += (fff_ways * ff_ways) * 2
        ways += (fff_ways * f_ways ** 2) * 3
        ways += (ffff_ways * f_ways) * 2
        ways += fffff_ways
        print(count, record, ways)
        count += 1
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
    # run_part1(True)
    run_part2(False)


if __name__ == "__main__":
    main()
