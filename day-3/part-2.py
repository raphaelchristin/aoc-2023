from solve import *


def main():
    with open("input.txt", "r") as input:
        lines = input.readlines()
    stars = get_stars(lines)
    gear_ratios = get_gear_ratios(lines, stars)
    return sum(gear_ratios)


if __name__ == "__main__":
    print(f"The result for part 2 is: {main()}")
