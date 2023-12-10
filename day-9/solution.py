def extrapolate_next(line):
    stack = [line]
    while any(stack[-1]):
        diffs = [b - a for a, b in zip(stack[-1], stack[-1][1:])]
        stack.append(diffs)
    carry = 0
    while stack:
        carry += stack.pop().pop()
    return carry


def main(file="input.txt"):
    with open(file, "r") as input:
        lines = input.readlines()
    lines = [[int(i) for i in line.split()] for line in lines]
    extrapolated_tail = [extrapolate_next(line) for line in lines]
    extrapolated_head = [extrapolate_next(line[::-1]) for line in lines]
    return sum(extrapolated_tail), sum(extrapolated_head)


if __name__ == "__main__":
    part1, part2 = main()
    print(f"The result for part 1 is: {part1}")
    print(f"The result for part 2 is: {part2}")
