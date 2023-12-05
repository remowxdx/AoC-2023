#!/usr/bin/env python3
"""
Advent of Code 2023, Day 5
"""

from aoc import check_solution, save_solution, test_eq

DAY = 5


def get_input(filename):
    with open(filename, "r", encoding="ascii") as input_file:
        lines = input_file.read()
    return lines.splitlines()


def parse_seeds(line):
    _, seeds = line.split(": ")
    return [int(seed) for seed in seeds.split(" ")]


def parse_map_type(line):
    map_type, _ = line.split(" ")
    source, _, destination = map_type.split("-")
    print(source, destination)
    return source, destination


def parse_maps(data):
    maps = {}
    status = "empty"
    for line in data:
        if line == "":
            status = "empty"
            continue
        if status == "empty":
            map_type = parse_map_type(line)
            maps[map_type] = []
            status = "map"
            continue
        if status == "map":
            # seed-to-soil: soil_start seed_start range
            maps[map_type].append([int(num) for num in line.split(" ")])
    return maps


def map_src_to_dst(map_, value):
    for dst, src, rng in map_:
        if src <= value < src + rng:
            return dst + value - src
    return value


def seed_to_location(maps, seed):
    from_ = "seed"
    to = "location"
    value = seed
    while from_ != to:
        print(value, end="->")
        for src, dst in maps.keys():
            if src == from_:
                value = map_src_to_dst(maps[(src, dst)], value)
                from_ = dst
    print(value)
    return value


def part1(data):
    seeds = parse_seeds(data[0])

    maps = parse_maps(data[2:])

    locations = []
    for seed in seeds:
        locations.append(seed_to_location(maps, seed))
    return min(locations)


def part2(data):
    return None


def run_tests():
    test_input_1 = get_input(f"ex{DAY}")
    print("Test Part 1:")
    test_eq("Test 1.1", part1, 35, test_input_1)
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
    run_part1(False)
    # run_part2(False)


if __name__ == "__main__":
    main()
