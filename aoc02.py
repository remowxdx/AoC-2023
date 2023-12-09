#!/usr/bin/env python3
"""
Advent of Code 2023, Day 2
"""

from aoc import check_solution, save_solution, test_eq

DAY = 2


def get_input(filename):
    with open(filename, "r", encoding="ascii") as input_file:
        lines = input_file.read()
    return lines.splitlines()


def parse_draw(draw):
    colors = {"red": 0, "green": 0, "blue": 0}
    for cubes in draw.split(", "):
        qty, color = cubes.split(" ")
        colors[color] = int(qty)
    return colors


def parse_draws(draws):
    result = []
    for draw in draws.split("; "):
        result.append(parse_draw(draw))
    return result


def parse_game(line):
    label, draws = line.split(": ")
    game = {}
    _, game_id_str = label.split(" ")
    game["id"] = int(game_id_str)
    game["draws"] = parse_draws(draws)
    red, green, blue = 0, 0, 0
    game["red"] = 0
    game["green"] = 0
    game["blue"] = 0
    for draw in game["draws"]:
        red = max(red, draw["red"])
        green = max(green, draw["green"])
        blue = max(blue, draw["blue"])
    game["red"] = red
    game["green"] = green
    game["blue"] = blue
    return game


def power(game):
    return game["red"] * game["green"] * game["blue"]


def game_possible(line, bag):
    game = parse_game(line)
    if game["red"] <= bag[0] and game["green"] <= bag[1] and game["blue"] <= bag[2]:
        return game["id"]
    return 0


def part1(data):
    id_sum = 0
    for line in data:
        id_sum += game_possible(line, (12, 13, 14))
    return id_sum


def part2(data):
    power_sum = 0
    for line in data:
        power_sum += power(parse_game(line))
    return power_sum


def run_tests():
    test_input_1 = get_input(f"examples/ex{DAY}")
    print("Test Part 1:")
    test_eq("Test 1.1", part1, 8, test_input_1)
    print()

    print("Test Part 2:")
    test_eq("Test 2.1", part2, 2286, test_input_1)
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
