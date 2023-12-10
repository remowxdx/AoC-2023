#!/usr/bin/env python3
"""
Advent of Code 2023, Day 10
"""

from aoc import check_solution, save_solution, test_eq

DAY = 10


def get_input(filename):
    with open(filename, "r", encoding="ascii") as input_file:
        lines = input_file.read()
    return lines.splitlines()


def cell_connections(row, col, char):
    connections = {
        ".": [],
        "|": [(-1, 0), (1, 0)],
        "-": [(0, -1), (0, 1)],
        "L": [(-1, 0), (0, 1)],
        "J": [(-1, 0), (0, -1)],
        "7": [(0, -1), (1, 0)],
        "F": [(0, 1), (1, 0)],
        "S": [],
    }
    return [
        (row + connection[0], col + connection[1]) for connection in connections[char]
    ]


def fill_start(grid):
    start = grid["S"]
    for direction in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        cell = (start[0] + direction[0], start[1] + direction[1])
        if cell in grid and start in grid[cell]:
            grid[start].append(cell)


def parse_grid(data):
    grid = {}
    for row, line in enumerate(data):
        for col, char in enumerate(line):
            if char == "S":
                grid["S"] = (row, col)
            grid[(row, col)] = cell_connections(row, col, char)
    fill_start(grid)
    return grid


def next_cell(cell, prev, grid):
    for candidate in grid[cell]:
        if candidate != prev:
            return candidate, cell
    return None


def follow_pipes(grid):
    # print(0, grid["S"])
    prev1 = grid["S"]
    prev2 = grid["S"]
    side1 = grid[grid["S"]][0]
    side2 = grid[grid["S"]][1]
    count = 1
    while side1 != side2:
        # print(count, side1, side2)
        side1, prev1 = next_cell(side1, prev1, grid)
        side2, prev2 = next_cell(side2, prev2, grid)
        count += 1
    # print(count, side1)
    return count


def recell(cell, connections):
    iocells = {}
    row, col = cell
    directions = [
        (connection[0] - row, connection[1] - col) for connection in connections
    ]
    new_row = row * 3 + 1
    new_col = col * 3 + 1
    iocells[(new_row, new_col)] = [
        (direction[0] + new_row, direction[1] + new_col) for direction in directions
    ]
    for direction in directions:
        iocells[(new_row + direction[0], new_col + direction[1])] = [
            (new_row, new_col),
            (new_row + 2 * direction[0], new_col + 2 * direction[1]),
        ]
    return iocells


def regrid(grid):
    io_grid = {}
    for cell, connections in grid.items():
        if cell == "S":
            io_grid["S"] = (connections[0] * 3 + 1, connections[1] * 3 + 1)
            continue
        if len(connections) == 0:
            continue
        iocells = recell(cell, connections)
        for iocell, ioconnections in iocells.items():
            io_grid[iocell] = ioconnections
    return io_grid


def find_loop(grid):
    start = grid["S"]
    prev = start
    cur = grid[start][0]
    loop = set((start,))
    while cur != start:
        loop.add(cur)
        cur, prev = next_cell(cur, prev, grid)
    return loop


def find_outside(grid, loop):
    max_row = 0
    max_col = 0
    for cell in grid:
        if cell == "S":
            continue
        max_row = max(max_row, cell[0] + 1)
        max_col = max(max_col, cell[1] + 1)

    outside = set()
    to_visit = [(0, 0)]
    while len(to_visit) > 0:
        cell = to_visit.pop()
        if cell in loop:
            continue
        outside.add(cell)
        for direction in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            new_cell = (cell[0] + direction[0], cell[1] + direction[1])
            if new_cell[0] < 0 or new_cell[0] > max_row:
                continue
            if new_cell[1] < 0 or new_cell[1] > max_col:
                continue
            if new_cell not in loop and new_cell not in outside:
                to_visit.append(new_cell)
    return outside


def count_insides(grid, outside, loop):
    count = 0
    for cell in grid:
        if cell == "S":
            continue
        io_cell = (cell[0] * 3 + 1, cell[1] * 3 + 1)
        if io_cell in outside or io_cell in loop:
            continue
        count += 1
    return count


def part1(data):
    grid = parse_grid(data)
    return follow_pipes(grid)


def part2(data):
    grid = parse_grid(data)
    io_grid = regrid(grid)
    loop = find_loop(io_grid)
    outside = find_outside(io_grid, loop)
    # print(outside)
    return count_insides(grid, outside, loop)


def run_tests():
    test_input_1 = get_input(f"examples/ex{DAY}.1")
    test_input_2 = get_input(f"examples/ex{DAY}.2")
    print("Test Part 1:")
    test_eq("Test 1.1", part1, 4, test_input_1)
    test_eq("Test 1.2", part1, 8, test_input_2)
    print()

    test_input_3 = get_input(f"examples/ex{DAY}.3")
    test_input_4 = get_input(f"examples/ex{DAY}.4")
    print("Test Part 2:")
    test_eq("Test 1.3", part2, 8, test_input_3)
    test_eq("Test 1.4", part2, 10, test_input_4)
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
