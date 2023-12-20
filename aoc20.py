#!/usr/bin/env python3
"""
Advent of Code 2023, Day 20
"""

from aoc import check_solution, save_solution, test_eq

DAY = 20


class System:
    def __init__(self, description):
        self.modules = {}
        # self.connections = {}
        self.sources = {}
        self.destinations = {}
        self.to_pulse = []
        for line in description:
            module, destinations = line.split(" -> ")
            if module == "broadcaster":
                name = module
                type_ = "b"
            elif module[0] in ["&", "%"]:
                name = module[1:]
                type_ = module[0]
            else:
                name = module
                type_ = "u"
            self.modules[name] = Module(name, type_, destinations.split(", "))

            for dst in destinations.split(", "):
                # self.connections[(name, dst)] = 0
                if name not in self.destinations:
                    self.destinations[name] = []
                self.destinations[name].append(dst)
                if dst not in self.sources:
                    self.sources[dst] = []
                self.sources[dst].append(name)

        to_add = []
        for name, module in self.modules.items():
            if module.type == "&":
                for src in self.sources[name]:
                    module.add_source(src)
            for dst in self.destinations[name]:
                if dst not in self.modules:
                    to_add.append(dst)
        for module in to_add:
            self.modules[module] = Module(module, "u", [])

    def run(self):
        self.to_pulse = [("button", "broadcaster", 0)]
        count = [0, 0]
        while len(self.to_pulse) > 0:
            src, dst, pulse = self.to_pulse.pop(0)
            # print(f"{src} -{pulse}-> {dst}")
            count[pulse] += 1
            self.to_pulse.extend(self.modules[dst].recv(src, pulse))
        return count


class Module:
    def __init__(self, name, type_, destinations):
        self.name = name
        self.type = type_
        self.state = 0
        self.received = None
        self.sources = {}
        self.destinations = destinations

    def add_source(self, source):
        self.sources[source] = 0

    def recv(self, source, pulse):
        if self.type == "%":
            if pulse == 1:
                return []
            self.state = 1 - self.state
            return [(self.name, dst, self.state) for dst in self.destinations]
        if self.type == "&":
            self.sources[source] = pulse
            for state in self.sources.values():
                if state == 0:
                    return [(self.name, dst, 1) for dst in self.destinations]
            return [(self.name, dst, 0) for dst in self.destinations]
        if self.type == "b":
            return [(self.name, dst, pulse) for dst in self.destinations]
        if self.type == "u":
            # print("Output:", pulse)
            return []
        raise ValueError("Unknown module.")


def get_input(filename):
    with open(filename, "r", encoding="ascii") as input_file:
        lines = input_file.read()
    return lines.splitlines()


def part1(data):
    system = System(data)
    # print(", ".join([module for module in system.modules]))
    total = [0, 0]
    for _ in range(1000):
        count = system.run()
        # print(count)
        total[0] += count[0]
        total[1] += count[1]
    return total[0] * total[1]


def part2(data):
    return None


def run_tests():
    test_input_1 = get_input(f"examples/ex{DAY}.1")
    test_input_2 = get_input(f"examples/ex{DAY}.2")
    print("Test Part 1:")
    test_eq("Test 1.1", part1, 32000000, test_input_1)
    test_eq("Test 1.2", part1, 11687500, test_input_2)
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
