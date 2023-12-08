#!/usr/bin/env python3
"""
Advent of Code 2023, Day 8
"""

from aoc import check_solution, save_solution, test_eq

DAY = 8


def get_input(filename):
    with open(filename, "r", encoding="ascii") as input_file:
        lines = input_file.read()
    return lines.splitlines()


def parse_input(data):
    instructions = data[0]

    nodes = {}
    for line in data[2:]:
        node, l_r = line.split(" = ")
        left, right = l_r.strip("()").split(", ")
        nodes[node] = (left, right)
    return instructions, nodes


def part1(data):
    instructions, nodes = parse_input(data)
    node = "AAA"
    instruction = 0
    while node != "ZZZ":
        if instructions[instruction % len(instructions)] == "L":
            node = nodes[node][0]
        else:
            node = nodes[node][1]
        instruction += 1
    return instruction


def at_end(nodes):
    for node in nodes:
        if not node.endswith("Z"):
            return False
    return True


def step_nodes(cur_nodes, instruction, nodes):
    next_nodes = []
    for node in cur_nodes:
        if instruction == "L":
            next_nodes.append(nodes[node][0])
        else:
            next_nodes.append(nodes[node][1])
    return next_nodes


def next_node(node, instruction, nodes):
    if instruction == "L":
        return nodes[node][0]
    return nodes[node][1]


def find_cycle(node, nodes, instructions):
    print(node)
    cycle = []
    visited = []
    count = 0
    mod = len(instructions)

    instruction = instructions[count % mod]
    visited.append((node, count % mod))
    node = next_node(node, instruction, nodes)
    count += 1
    while True:
        instruction = instructions[count % mod]
        if (node, count % mod) in visited:
            print(count)
            cycle.append(count - visited.index((node, count % mod)))
            visited.append((node, count % mod))
            break
        visited.append((node, count % mod))
        if node.endswith("Z"):
            cycle.append(count)
        node = next_node(node, instruction, nodes)
        count += 1
    return cycle


def combine(cycles):
    cys = [cycles[node] for node in cycles]

    while len(cys) > 1:
        c1 = cys.pop()
        c2 = cys.pop()
        base = c1[0]
        while (base - c2[0]) % c2[1] != 0:
            base += c1[1]
        period = c1[1]
        while period % c2[1] != 0:
            period += c1[1]
        cys.append([base, period])
    return cys[0]


def part2(data):
    instructions, nodes = parse_input(data)
    cur_nodes = []
    cycles = {}
    for node in nodes:
        if node.endswith("A"):
            cur_nodes.append(node)
            cycles[node] = find_cycle(node, nodes, instructions)

    print(cycles)
    if "22A" in cycles:
        cycles["22A"] = [3, 3]
    print(cycles)
    c = combine(cycles)
    return c[0]

    max_cycle = max([cycles[node][1] for node in cycles])
    for node, cycle in cycles.items():
        if cycle[1] == max_cycle:
            max_node = node
    print(max_node, max_cycle)
    base = cycles[max_node][0]
    candidate = base + max_cycle
    while True:
        print(candidate)
        for node, cycle in cycles.items():
            # n = b + k * c  => n - b = k * c => (n-b) % c == 0
            if (candidate - cycle[0]) % cycle[1] != 0:
                print("no", node)
                break
            else:
                print("yes", node)
        else:
            return candidate
        candidate += max_cycle

    return 0


def run_tests():
    test_input_1 = get_input(f"ex{DAY}.1")
    test_input_2 = get_input(f"ex{DAY}.2")
    test_input_3 = get_input(f"ex{DAY}.3")
    print("Test Part 1:")
    test_eq("Test 1.1", part1, 2, test_input_1)
    test_eq("Test 1.2", part1, 6, test_input_2)
    print()

    print("Test Part 2:")
    test_eq("Test 2.1", part2, 6, test_input_3)
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
    run_part1(True)
    run_part2(True)


if __name__ == "__main__":
    main()
