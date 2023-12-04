#!/usr/bin/env python3
"""
Advent of Code 2023, Day 4
"""

from aoc import check_solution, save_solution, test_eq

DAY = 4


def get_input(filename):
    with open(filename, "r", encoding="ascii") as input_file:
        lines = input_file.read()
    return lines.splitlines()


def parse_card(line):
    res = {"id": 0, "winning": [], "have": [], "qty": 1}
    card_id, card = line.split(": ")
    for num in card_id.split(" "):
        if num.isnumeric():
            res["id"] = int(num)
    win_str, have_str = card.split(" | ")
    for win in win_str.split(" "):
        if win.isnumeric():
            res["winning"].append(int(win))
    for have in have_str.split(" "):
        if have.isnumeric():
            res["have"].append(int(have))
    return res


def value(card):
    points = 0
    for have in card["have"]:
        if have in card["winning"]:
            if points == 0:
                points = 1
            else:
                points *= 2
    return points


def winning(card):
    winners = 0
    for have in card["have"]:
        if have in card["winning"]:
            winners += 1
    return winners


def part1(data):
    points = 0
    for line in data:
        points += value(parse_card(line))
    return points


def part2(data):
    cards = []
    for line in data:
        card = parse_card(line)
        cards.append(card)
    for idx, card in enumerate(cards):
        wins = winning(card)
        for i in range(wins):
            copied = idx + i + 1
            if copied < len(cards):
                cards[copied]["qty"] += card["qty"]
    num_cards = sum([card["qty"] for card in cards])
    return num_cards


def run_tests():
    test_input_1 = get_input(f"ex{DAY}")
    print("Test Part 1:")
    test_eq("Test 1.1", part1, 13, test_input_1)
    print()

    print("Test Part 2:")
    test_eq("Test 2.1", part2, 30, test_input_1)
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
    run_part2(False)


if __name__ == "__main__":
    main()
