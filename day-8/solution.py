import math
import re


def main(file="input.txt"):
    with open(file, "r") as input:
        lines = input.readlines()
    moves = lines.pop(0).strip()
    lines = [
        re.sub(r"\(|\)|,|=", " ", line.strip()).split()
        for line in lines
        if line.strip()
    ]
    graph = {l[0]: (l[1], l[2]) for l in lines}
    starts = {n: 0 for n in graph.keys() if n.endswith("A")}
    for start in starts:
        current = start
        mvs = list(moves)
        while not current.endswith("Z"):
            if not mvs:
                mvs = list(moves)
            move = mvs.pop(0)
            starts[start] += 1
            if move == "R":
                current = graph[current][1]
            else:
                current = graph[current][0]
    return starts.get("AAA", 0), math.lcm(*starts.values())


if __name__ == "__main__":
    part1, part2 = main()
    print(f"The result for part 1 is: {part1}")
    print(f"The result for part 2 is: {part2}")
