#!/usr/bin/env python3
"""
Advent of Code 2023, Day 23
"""

from aoc import check_solution, save_solution, test_eq

DAY = 23


def get_input(filename):
    with open(filename, "r", encoding="ascii") as input_file:
        lines = input_file.read()
    return lines.splitlines()


def parse_map(data):
    grid = {}
    for row, line in enumerate(data):
        for col, char in enumerate(line):
            if char != "#":
                grid[(row, col)] = char
    return grid


def simpler_map(grid):
    smap = {}
    neighs = {}

    for pos in grid:
        neighs[pos] = neighbours_2(grid, pos)

    for pos, posn in neighs.items():
        if len(posn) == 2:
            continue
        print(pos)
        smap[pos] = {}
        for neigh in posn:
            prev = pos
            dist = 1
            while len(neighs[neigh]) == 2:
                print(neigh, "->", neighs[neigh])
                if neighs[neigh][0] == prev:
                    prev = neigh
                    neigh = neighs[neigh][1]
                else:
                    prev = neigh
                    neigh = neighs[neigh][0]
                dist += 1
            smap[pos][neigh] = dist
    return smap


def neighbours(grid, pos):
    row, col = pos
    dirs = {
        ">": (row, col + 1),
        "v": (row + 1, col),
        "^": (row - 1, col),
        "<": (row, col - 1),
    }
    char = grid[pos]
    if char in dirs:
        return [dirs[char]]
    return [new_pos for new_pos in dirs.values() if new_pos in grid]


def neighbours_2(grid, pos):
    row, col = pos
    dirs = {
        ">": (row, col + 1),
        "v": (row + 1, col),
        "^": (row - 1, col),
        "<": (row, col - 1),
    }
    return [new_pos for new_pos in dirs.values() if new_pos in grid]


def wander(grid, start, end):
    to_visit = {start: [start]}
    visited = {}
    while len(to_visit) > 0:
        pos, path = to_visit.popitem()
        # print(pos, path)
        if pos in visited:
            if len(path) > len(visited[pos]):
                visited[pos] = path
        else:
            visited[pos] = path
        if pos == end:
            continue
        for next_pos in neighbours(grid, pos):
            if next_pos in path:
                continue
            new_path = path.copy()
            new_path.append(next_pos)
            to_visit[next_pos] = new_path
    return visited


def path_len(path):
    return path[-1][1]


def pos_in_path(pos, path):
    for ppos, plen in path:
        if pos == ppos:
            return True
    return False


def wander_2(grid, start, end):
    to_visit = [[(start, 0)]]
    visited = {}
    while len(to_visit) > 0:
        path = to_visit.pop()
        pos, pos_path_len = path[-1]
        # print(pos, path)
        if pos in visited:
            # print(pos_path_len, visited[pos])
            if pos_path_len > path_len(visited[pos]):
                # print(pos, pos_path_len, len(to_visit))
                if end in visited:
                    print("end", visited[end][-1][1])
                visited[pos] = path
        else:
            visited[pos] = path
        if pos == end:
            continue
        for next_pos in grid[pos]:
            if pos_in_path(next_pos, path):
                continue
            new_path = path.copy()
            new_path.append((next_pos, pos_path_len + grid[pos][next_pos]))
            to_visit.append(new_path)
    return visited


def part1(data):
    grid = parse_map(data)
    end = (0, 0)
    for pos in grid:
        if pos[0] > end[0]:
            end = pos
    paths = wander(grid, (0, 1), end)

    return len(paths[end]) - 1


def part2(data):
    grid = parse_map(data)
    end = (0, 0)
    for pos in grid:
        if pos[0] > end[0]:
            end = pos
    s_map = simpler_map(grid)

    print(s_map)

    paths = wander_2(s_map, (0, 1), end)

    return paths[end][-1][1]


def run_tests():
    test_input_1 = get_input(f"examples/ex{DAY}")
    print("Test Part 1:")
    test_eq("Test 1.1", part1, 94, test_input_1)
    print()

    print("Test Part 2:")
    test_eq("Test 2.1", part2, 154, test_input_1)
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
    run_part2(True)


if __name__ == "__main__":
    main()
