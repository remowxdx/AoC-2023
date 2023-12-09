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


def parse_seed_ranges(line):
    _, seeds = line.split(": ")
    start = None
    seed_ranges = []
    for num in seeds.split(" "):
        if start is None:
            start = int(num)
        else:
            seed_ranges.append((start, start + int(num)))
            start = None
    return seed_ranges


def parse_map_type(line):
    map_type, _ = line.split(" ")
    source, _, destination = map_type.split("-")
    # print(source, destination)
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
        # print(value, end="->")
        for src, dst in maps.keys():
            if src == from_:
                value = map_src_to_dst(maps[(src, dst)], value)
                from_ = dst
    # print(value)
    return value


def map_src_rng_to_dst_rngs(map_, range_):
    map_rngs = {}
    map_limits = set()
    for dst, src, rng in map_:
        map_src_start = src
        map_src_end = src + rng
        map_dst_start = dst
        map_dst_end = dst + rng
        map_rngs[(map_src_start, map_src_end)] = (map_dst_start, map_dst_end)
        map_limits.add(map_src_start)
        map_limits.add(map_src_end)
    map_limits.add(range_[0])
    map_limits.add(range_[1])
    # print("lim", sorted(map_limits))

    split_values = []
    for limit in sorted(map_limits):
        if range_[0] <= limit <= range_[1]:
            split_values.append(limit)

    split_ranges = []
    for num, value in enumerate(split_values[:-1]):
        split_ranges.append((value, split_values[num + 1]))
    print("rng:", split_ranges)
    dst_rngs = []
    for src_start, src_end in split_ranges:
        done = False
        # print("rngs:", map_rngs)
        for map_src, map_dst in map_rngs.items():
            map_src_start, map_src_end = map_src
            if src_end <= map_src_start or src_start >= map_src_end:
                continue
            # print("src:", map_src, "dst:", map_dst)
            map_dst_start, map_dst_end = map_dst
            delta = map_dst_start - map_src_start
            dst_start = src_start + delta
            dst_end = src_end + delta
            dst_rngs.append((dst_start, dst_end))
            done = True
        if not done:
            dst_rngs.append((src_start, src_end))

    print(range_, end=" -> ")
    print("dsts:", dst_rngs)
    return dst_rngs


def map_src_rngs_to_dst_rngs(map_, rngs):
    dst_rngs = []
    for rng in rngs:
        dst_rng = map_src_rng_to_dst_rngs(map_, rng)
        dst_rngs.extend(dst_rng)
    return dst_rngs


def seed_range_to_locations(maps, seed_range):
    from_ = "seed"
    to = "location"
    rngs = [seed_range]
    while from_ != to:
        for src, dst in maps.keys():
            if src == from_:
                print("=============", src, rngs, end="->")
                rngs = map_src_rngs_to_dst_rngs(maps[(src, dst)], rngs)
                from_ = dst
    print("locations:", rngs)
    return rngs


def part1(data):
    seeds = parse_seeds(data[0])

    maps = parse_maps(data[2:])

    locations = []
    for seed in seeds:
        locations.append(seed_to_location(maps, seed))
    return min(locations)


def part2(data):
    seeds = parse_seed_ranges(data[0])

    maps = parse_maps(data[2:])

    locations = []
    for seed_range in seeds:
        locs = seed_range_to_locations(maps, seed_range)
        locations.extend(locs)
    return min([location[0] for location in locations])


def run_tests():
    test_input_1 = get_input(f"examples/ex{DAY}")
    print("Test Part 1:")
    test_eq("Test 1.1", part1, 35, test_input_1)
    print()

    print("Test Part 2:")
    test_eq("Test 2.1", part2, 46, test_input_1)
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
