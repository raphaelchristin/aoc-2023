from solve import *


def main():
    with open("input.txt", "r") as input:
        lines = input.readlines()
    return sum([get_line_num(line, True) for line in lines])


if __name__ == "__main__":
    print(f"The result for part 2 is: {main()}")
