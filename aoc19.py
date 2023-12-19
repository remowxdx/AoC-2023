#!/usr/bin/env python3
"""
Advent of Code 2023, Day 19
"""

from aoc import check_solution, save_solution, test_eq

DAY = 19


class Rule:
    def __init__(self, rule_str):
        if ":" in rule_str:
            cond, next_workflow = rule_str.split(":")
            self.cat = cond[0]
            self.comp = cond[1]
            self.value = int(cond[2:])
            self.next = next_workflow
        else:
            self.cat = "e"
            self.comp = ""
            self.value = 0
            self.next = rule_str

    def next_workflow(self, part):
        if self.cat == "e":
            return self.next
        if self.comp == ">":
            if part[self.cat] > self.value:
                return self.next
            return None
        if self.comp == "<":
            if part[self.cat] < self.value:
                return self.next
            return None
        raise ValueError("Unknown rule.")

    def dispatch(self, part):
        if self.cat == "e":
            return part, self.next, None
        frm, to = part[self.cat]
        if self.comp == ">":
            if to > self.value:
                sent = {
                    "x": [part["x"][0], part["x"][1]],
                    "m": [part["m"][0], part["m"][1]],
                    "a": [part["a"][0], part["a"][1]],
                    "s": [part["s"][0], part["s"][1]],
                }
                thru = {
                    "x": [part["x"][0], part["x"][1]],
                    "m": [part["m"][0], part["m"][1]],
                    "a": [part["a"][0], part["a"][1]],
                    "s": [part["s"][0], part["s"][1]],
                }
                sent[self.cat][0] = max(frm, self.value + 1)
                thru[self.cat][1] = max(frm, self.value)
                return sent, self.next, thru
            else:
                return None, None, part
        else:
            if frm < self.value:
                sent = {
                    "x": [part["x"][0], part["x"][1]],
                    "m": [part["m"][0], part["m"][1]],
                    "a": [part["a"][0], part["a"][1]],
                    "s": [part["s"][0], part["s"][1]],
                }
                thru = {
                    "x": [part["x"][0], part["x"][1]],
                    "m": [part["m"][0], part["m"][1]],
                    "a": [part["a"][0], part["a"][1]],
                    "s": [part["s"][0], part["s"][1]],
                }
                sent[self.cat][1] = min(to, self.value - 1)
                thru[self.cat][0] = min(to, self.value)
                return sent, self.next, thru
            else:
                return None, None, part


def get_input(filename):
    with open(filename, "r", encoding="ascii") as input_file:
        lines = input_file.read()
    return lines.splitlines()


def parse_workflow_parts(data):
    parse = "workflow"
    workflows = {}
    parts = []
    for line in data:
        if line == "":
            parse = "parts"
            continue
        if parse == "workflow":
            name, workflow = parse_workflow(line)
            workflows[name] = workflow
        else:
            parts.append(parse_part(line))
    return workflows, parts


def parse_workflow(line):
    name, rules_str = line.split("{")
    rules = [Rule(rule) for rule in rules_str[:-1].split(",")]
    return name, rules


def parse_part(line):
    part = {}
    cats = line[1:-1].split(",")
    for cat in cats:
        part[cat[0]] = int(cat[2:])
    return part


def is_accepted(part, workflow, workflows):
    for rule in workflows[workflow]:
        next_ = rule.next_workflow(part)
        if next_ is None:
            continue
        if next_ == "R":
            return False
        if next_ == "A":
            return True
        return is_accepted(part, next_, workflows)


def sum_of_parts(parts):
    total = 0
    for part in parts:
        total += sum(part.values())
    return total


def accepted_parts(part, workflow, workflows):
    if workflow == "A":
        return [part]
    if workflow == "R":
        return []
    accepted = []
    part_thru = part
    for rule in workflows[workflow]:
        if part_thru is None:
            break
        part_sent, next_workflow, part_thru = rule.dispatch(part_thru)
        if part_sent is not None:
            accepted.extend(accepted_parts(part_sent, next_workflow, workflows))
    # print(workflow, accepted)
    return accepted


def part1(data):
    rules, parts = parse_workflow_parts(data)
    accepted = []
    for part in parts:
        if is_accepted(part, "in", rules):
            accepted.append(part)
    result = sum_of_parts(accepted)
    return result


def part2(data):
    workflows, _ = parse_workflow_parts(data)
    accepted = accepted_parts(
        {"x": [1, 4000], "m": [1, 4000], "a": [1, 4000], "s": [1, 4000]},
        "in",
        workflows,
    )
    return sum(
        [
            (1 + p["x"][1] - p["x"][0])
            * (1 + p["m"][1] - p["m"][0])
            * (1 + p["a"][1] - p["a"][0])
            * (1 + p["s"][1] - p["s"][0])
            for p in accepted
        ]
    )


def run_tests():
    test_input_1 = get_input(f"examples/ex{DAY}")
    print("Test Part 1:")
    test_eq("Test 1.1", part1, 19114, test_input_1)
    print()

    print("Test Part 2:")
    test_eq("Test 2.1", part2, 167409079868000, test_input_1)
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
