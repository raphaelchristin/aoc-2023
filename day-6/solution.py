import re


def compute_record_breaking_product(times, distances):
    product = 1
    for t, d in zip(times, distances):
        no_record = 0
        hold_time = 0
        while hold_time < t:
            dst = hold_time * (t - hold_time)
            if dst > d:
                break
            hold_time += 1
            no_record += 1
        product *= t - no_record * 2 + 1
    return product


def main(file="input.txt"):
    with open(file, "r") as input:
        lines = input.readlines()
    times = [int(t) for t in re.findall(r"(\d+)", lines[0])]
    distances = [int(d) for d in re.findall(r"(\d+)", lines[1])]
    time = [int("".join([str(t) for t in times]))]
    distance = [int("".join([str(d) for d in distances]))]
    many_races_product = compute_record_breaking_product(times, distances)
    one_race_product = compute_record_breaking_product(time, distance)
    return many_races_product, one_race_product


if __name__ == "__main__":
    part1, part2 = main()
    print(f"The result for part 1 is: {part1}")
    print(f"The result for part 2 is: {part2}")
