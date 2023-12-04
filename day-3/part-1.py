from solve import *


def main():
    with open("input.txt", "r") as input:
        lines = input.readlines()
    symbols = get_symbols_positions(lines)
    part_nums = [
        get_part_numbers_sum(line, idx, symbols) for idx, line in enumerate(lines)
    ]
    return sum(part_nums)


if __name__ == "__main__":
    print(f"The result for part 1 is: {main()}")
