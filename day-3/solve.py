import math as m
import re


def get_symbols_positions(lines):
    symbols = dict()
    for row in range(len(lines)):
        for col in range(len(lines[0])):
            if lines[row][col] not in "0123456789.\n":
                symbols[(row, col)] = []
    return symbols


def get_stars(lines):
    stars = dict()
    for row in range(len(lines)):
        for col in range(len(lines[0])):
            if lines[row][col] in "*":
                stars[(row, col)] = []
    return stars


def get_part_numbers_sum(line, row_index, symbols):
    pattern = re.compile(r"(\d+)")
    iter = re.finditer(pattern, line)
    spans = [m.span(1) for m in iter]
    nums = re.findall(pattern, line)
    part_nums = []
    for num, span in zip(nums, spans):
        lower, upper = span
        surround = [
            (row, col)
            for row in range(row_index - 1, row_index + 2)
            for col in range(lower - 1, upper + 1)
        ]
        if any([True if s in symbols else False for s in surround]):
            part_nums.append(int(num))
    return sum(part_nums)


def get_gear_ratios(lines, stars):
    pattern = re.compile(r"(\d+)")
    for ridx, line in enumerate(lines):
        iter = re.finditer(pattern, line)
        spans = [m.span(1) for m in iter]
        nums = re.findall(pattern, line)
        for num, span in zip(nums, spans):
            lower, upper = span
            surround = [
                (row, col)
                for row in range(ridx - 1, ridx + 2)
                for col in range(lower - 1, upper + 1)
            ]
            for s in surround & stars.keys():
                stars[s].append(int(num))

    return [m.prod(g) for g in stars.values() if len(g) == 2]
