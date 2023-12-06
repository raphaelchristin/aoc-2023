def main(file="input.txt"):
    with open(file, "r") as input:
        lines = input.readlines()
    return 0, 0


if __name__ == "__main__":
    part1, part2 = main()
    print(f"The result for part 1 is: {part1}")
    print(f"The result for part 2 is: {part2}")
