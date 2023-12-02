from solve import get_line_num


def main():
    with open("input.txt", "r") as input:
        lines = input.readlines()
    return sum([get_line_num(line) for line in lines])


if __name__ == "__main__":
    print(f"The result for part 1 is: {main()}")
