#!/usr/bin/env python3
"""
Advent of Code 2023, Day 17
"""

from aoc import check_solution, save_solution, test_eq

DAY = 17


def get_input(filename):
    with open(filename, "r", encoding="ascii") as input_file:
        lines = input_file.read()
    return lines.splitlines()


def parse_city(data):
    city = []
    for line in data:
        city.append([int(heath) for heath in line])
    return city


def pop_block(to_visit):
    min_heath = min(to_visit.keys())
    block = to_visit[min_heath].pop()
    if len(to_visit[min_heath]) == 0:
        del to_visit[min_heath]
    return min_heath, block


def add_block(block, heath, to_visit):
    for b_heath, blocks in to_visit.items():
        if block in blocks:
            if b_heath <= heath:
                return
            to_visit[b_heath].remove(block)
            if len(to_visit[b_heath]) == 0:
                del to_visit[b_heath]
    if heath in to_visit:
        to_visit[heath].append(block)
    else:
        to_visit[heath] = [block]


def block_heath(block, city):
    return city[block[0]][block[1]]


def next_blocks(block, city):
    next_dir = {
        ">": [(0, 1, ">"), (1, 0, "v"), (-1, 0, "^")],
        "<": [(0, -1, "<"), (1, 0, "v"), (-1, 0, "^")],
        "v": [(1, 0, "v"), (0, -1, "<"), (0, 1, ">")],
        "^": [(-1, 0, "^"), (0, -1, "<"), (0, 1, ">")],
    }
    height = len(city)
    width = len(city[0])
    row, col, direction = block
    next_dirs = next_dir[direction[0]]
    candidate_blocks = []
    for dir_ in next_dirs:
        if dir_[2] == direction[0]:
            candidate_blocks.append((row + dir_[0], col + dir_[1], direction + dir_[2]))
        else:
            candidate_blocks.append((row + dir_[0], col + dir_[1], dir_[2]))
    next_blocks = []
    for row, col, direction in candidate_blocks:
        if (
            row >= 0
            and col >= 0
            and row < height
            and col < width
            and len(direction) < 4
        ):
            next_blocks.append((row, col, direction))
    return next_blocks


def find_min_path(start, city):
    visited = set()
    to_visit = {}
    to_visit[0] = [start]
    height = len(city)
    width = len(city[0])
    max_far = 0
    while len(to_visit) > 0:
        heath, block = pop_block(to_visit)
        far = block[0] + block[1]
        if far > max_far:
            max_far = far
            print(heath, block, len(visited), len(to_visit))
        if block in visited:
            continue
        # print(heath, block, end="")
        visited.add(block)
        if block[0] == height - 1 and block[1] == width - 1:
            return heath
        for next_block in next_blocks(block, city):
            add_block(next_block, heath + block_heath(next_block, city), to_visit)
        # print(next_blocks(block, city))
    return None


def next_blocks_ultra(block, city):
    next_dir = {
        ">": [(0, 1, ">"), (1, 0, "v"), (-1, 0, "^")],
        "<": [(0, -1, "<"), (1, 0, "v"), (-1, 0, "^")],
        "v": [(1, 0, "v"), (0, -1, "<"), (0, 1, ">")],
        "^": [(-1, 0, "^"), (0, -1, "<"), (0, 1, ">")],
    }
    height = len(city)
    width = len(city[0])
    row, col, direction = block
    next_dirs = next_dir[direction[0]]
    candidate_blocks = []
    for dir_ in next_dirs:
        if dir_[2] == direction[0]:
            candidate_blocks.append((row + dir_[0], col + dir_[1], direction + dir_[2]))
        elif len(direction) > 3:
            candidate_blocks.append((row + dir_[0], col + dir_[1], dir_[2]))
    next_blocks = []
    for row, col, direction in candidate_blocks:
        if (
            row >= 0
            and col >= 0
            and row < height
            and col < width
            and len(direction) < 11
        ):
            next_blocks.append((row, col, direction))
    return next_blocks


def find_min_path_ultra(start, city):
    visited = set()
    to_visit = {}
    to_visit[0] = [start]
    height = len(city)
    width = len(city[0])
    max_far = 0
    while len(to_visit) > 0:
        heath, block = pop_block(to_visit)
        far = block[0] + block[1]
        if far > max_far:
            max_far = far
            print(heath, block, len(visited), len(to_visit))
        if block in visited:
            continue
        # print(heath, block, end="")
        visited.add(block)
        if block[0] == height - 1 and block[1] == width - 1:
            return heath
        for next_block in next_blocks_ultra(block, city):
            add_block(next_block, heath + block_heath(next_block, city), to_visit)
        # print(next_blocks(block, city))
    return None


def part1(data):
    city = parse_city(data)
    min_path = find_min_path((0, 0, ">"), city)
    return min_path


def part2(data):
    city = parse_city(data)
    min_path = find_min_path_ultra((0, 0, "v"), city)
    return min_path


def run_tests():
    test_input_1 = get_input(f"examples/ex{DAY}")
    print("Test Part 1:")
    test_eq("Test 1.1", part1, 102, test_input_1)
    print()

    print("Test Part 2:")
    test_eq("Test 2.1", part2, 94, test_input_1)
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
