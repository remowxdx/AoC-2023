#!/usr/bin/env python3
"""
Advent of Code 2023, Day 22
"""

from aoc import check_solution, save_solution, test_eq

DAY = 22


def get_input(filename):
    with open(filename, "r", encoding="ascii") as input_file:
        lines = input_file.read()
    return lines.splitlines()


def parse_bricks(data):
    bricks = {}
    span = [0, 0]
    for idx, line in enumerate(data):
        frm, to = line.split("~")
        brick = (
            [int(num) for num in frm.split(",")],
            [int(num) for num in to.split(",")],
            idx,
        )
        z = brick[0][2]
        if z not in bricks:
            bricks[z] = []
        bricks[z].append(brick)
        span = [
            max(span[0], brick[0][0], brick[1][0]),
            max(span[1], brick[0][1], brick[1][1]),
        ]
    return bricks, (span[0] + 1, span[1] + 1)


def fall(brick, alt, space, ignore=None):
    supp_z = 0

    if ignore is not None and brick[2] == ignore[2]:
        return False

    for x in range(brick[0][0], brick[1][0] + 1):
        for y in range(brick[0][1], brick[1][1] + 1):
            supp_z = max(supp_z, alt[(x, y)])

    brick_height = brick[1][2] - brick[0][2]
    fallen = True
    if brick[0][2] == supp_z + 1:
        fallen = False

    brick[0][2] = supp_z + 1
    brick[1][2] = supp_z + 1 + brick_height

    for x in range(brick[0][0], brick[1][0] + 1):
        for y in range(brick[0][1], brick[1][1] + 1):
            alt[(x, y)] = brick[1][2]
            for z in range(brick[0][2], brick[1][2] + 1):
                space[(x, y)][z] = brick[2]
    return fallen


def is_free(brick, fallen_bricks, space):
    layer = brick[1][2]
    brick_id = brick[2]
    bricks_to_test = set()

    if layer + 1 not in fallen_bricks:
        return True

    for x in range(brick[0][0], brick[1][0] + 1):
        for y in range(brick[0][1], brick[1][1] + 1):
            if layer + 1 in space[(x, y)]:
                bricks_to_test.add(space[(x, y)][layer + 1])

    if len(bricks_to_test) == 0:
        return True

    supported = set()
    for z, bricks in fallen_bricks.items():
        for test in bricks:
            if test[2] in bricks_to_test:
                for x in range(test[0][0], test[1][0] + 1):
                    for y in range(test[0][1], test[1][1] + 1):
                        if layer in space[(x, y)]:
                            if space[(x, y)][layer] != brick_id:
                                supported.add(test[2])
    return len(supported) == len(bricks_to_test)


def part1(data):
    bricks, span = parse_bricks(data)
    alt = {}
    space = {}
    fallen_bricks = {}
    for x in range(span[0]):
        for y in range(span[1]):
            alt[(x, y)] = 0
            space[(x, y)] = {}
    for z in sorted(bricks.keys()):
        for old_brick in bricks[z]:
            brick = (old_brick[0].copy(), old_brick[1].copy(), old_brick[2])
            fall(brick, alt, space)
            new_z = brick[0][2]
            if new_z not in fallen_bricks:
                fallen_bricks[new_z] = []
            fallen_bricks[new_z].append(brick)
    free = 0
    for z in sorted(fallen_bricks.keys()):
        for brick in fallen_bricks[z]:
            if is_free(brick, fallen_bricks, space):
                free += 1
    return free


def part2(data):
    bricks, span = parse_bricks(data)
    alt = {}
    space = {}
    fallen_bricks = {}
    for x in range(span[0]):
        for y in range(span[1]):
            alt[(x, y)] = 0
            space[(x, y)] = {}
    for z in sorted(bricks.keys()):
        for old_brick in bricks[z]:
            brick = (old_brick[0].copy(), old_brick[1].copy(), old_brick[2])
            fall(brick, alt, space)
            new_z = brick[0][2]
            if new_z not in fallen_bricks:
                fallen_bricks[new_z] = []
            fallen_bricks[new_z].append(brick)

    fallen = 0
    for z in sorted(fallen_bricks.keys()):
        layer_bricks = fallen_bricks[z].copy()
        for rem_brick in layer_bricks:
            alt = {}
            space = {}
            refallen_bricks = {}
            for x in range(span[0]):
                for y in range(span[1]):
                    alt[(x, y)] = 0
                    space[(x, y)] = {}

            for zz in sorted(fallen_bricks.keys()):
                for old_brick in fallen_bricks[zz]:
                    brick = (old_brick[0].copy(), old_brick[1].copy(), old_brick[2])
                    if fall(brick, alt, space, rem_brick):
                        fallen += 1
                    new_z = brick[0][2]
                    if new_z not in refallen_bricks:
                        refallen_bricks[new_z] = []
                    refallen_bricks[new_z].append(brick)

    return fallen


def run_tests():
    test_input_1 = get_input(f"examples/ex{DAY}")
    print("Test Part 1:")
    test_eq("Test 1.1", part1, 5, test_input_1)
    print()

    print("Test Part 2:")
    test_eq("Test 2.1", part2, 7, test_input_1)
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
    run_part2(False)


if __name__ == "__main__":
    main()
