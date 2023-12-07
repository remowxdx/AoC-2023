#!/usr/bin/env python3
"""
Advent of Code 2023, Day 7
"""

from aoc import check_solution, save_solution, test_eq

DAY = 7


def get_input(filename):
    with open(filename, "r", encoding="ascii") as input_file:
        lines = input_file.read()
    return lines.splitlines()


class Hand:

    STRENGTH = {
        "A": 14,
        "K": 13,
        "Q": 12,
        "J": 11,
        "T": 10,
        "9": 9,
        "8": 8,
        "7": 7,
        "6": 6,
        "5": 5,
        "4": 4,
        "3": 3,
        "2": 2,
    }

    def __init__(self, line):
        hand, value, bid = self.parse_hand(line)
        self.hand = hand
        self.value = value
        self.bid = bid

    def strength(self, face):
        return self.STRENGTH[face]

    @staticmethod
    def parse_hand(line):
        hand, bid_str = line.split()
        bid = int(bid_str)
        value = {}
        for char in hand:
            if char not in value:
                value[char] = 0
            value[char] += 1
        return hand, value, bid

    def type(self):
        max_eq = max(self.value.values())
        min_eq = min(self.value.values())
        if max_eq == 5:
            return 7
        if max_eq == 4:
            return 6
        if max_eq == 3:
            if min_eq == 2:
                return 5
            return 4
        if max_eq == 2:
            count_pairs = 0
            for count in self.value.values():
                if count == 2:
                    count_pairs += 1
            if count_pairs == 2:
                return 3
            return 2
        if max_eq == 1:
            return 1

    def __gt__(self, other):
        if self.type() > other.type():
            return True
        if self.type() < other.type():
            return False
        for idx in range(5):
            ss = self.strength(self.hand[idx])
            os = other.strength(other.hand[idx])
            if ss != os:
                return ss > os

    def __str__(self):
        return f"Hand: {self.hand}, Bid: {self.bid}, Value: {self.value}"


def winnings(hands):
    total = 0
    for num, hand in enumerate(sorted(hands)):
        total += (num + 1) * hand.bid
    return total


def part1(data):
    hands = [Hand(line) for line in data]
    print()
    for hand in sorted(hands):
        print(hand)
    return winnings(hands)


def part2(data):
    return None


def run_tests():
    test_input_1 = get_input(f"ex{DAY}")
    print("Test Part 1:")
    test_eq("Test 1.1", part1, 6440, test_input_1)
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
    run_part1(True)
    # run_part2(False)


if __name__ == "__main__":
    main()
