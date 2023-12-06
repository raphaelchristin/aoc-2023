import re


def get_seeds(line):
    seeds = re.findall(r"(\d+)", line)
    return seeds


def get_seeds_ranges(seeds):
    seeds_list = [s for s in seeds]
    seeds = []
    while seeds_list:
        start = int(seeds_list.pop(0))
        rng = int(seeds_list.pop(0))
        seeds += [(start, rng)]
    return seeds


def build_map_ranges(seeds, lines):
    seed_ranges_map = {(int(seed), int(ln)) for (seed, ln) in seeds}
    new_ranges = set()
    changed_within_category = set()
    for line in lines:
        if not line.strip():
            continue
        if re.match(r"^\D+-to-(\D+) map:", line):
            changed_within_category.clear()
            continue
        dst, src, rng = tuple(re.findall(r"(\d+)", line))
        for seed, ln in seed_ranges_map:
            if (seed, ln) in changed_within_category:
                new_ranges.add((seed, ln))
                continue
            delta = int(src) - seed
            if (delta + int(rng) <= 0) or (int(src) >= seed + ln):
                new_ranges.add((seed, ln))
                continue
            if delta < 1:
                r_len = min(delta + int(rng), ln)
                new_ranges.add((int(dst) - delta, r_len))
                changed_within_category.add((int(dst) - delta, r_len))
                if r_len < ln:
                    new_ranges.add((seed + r_len, ln - r_len))
            else:
                new_ranges.add((seed, delta))
                r_len = min(ln - delta, int(rng))
                new_ranges.add((int(dst), r_len))
                changed_within_category.add((int(dst), r_len))
                if r_len < ln - delta:
                    new_ranges.add((seed + delta + r_len, ln - delta - r_len))
        seed_ranges_map = new_ranges
        new_ranges = set()
    return seed_ranges_map


def build_map(seeds, lines):
    seed_map = {seed: int(seed) for seed in seeds}
    changed_within_category = {seed: False for seed in seeds}
    for line in lines:
        if not line.strip():
            continue
        if re.match(r"^\D+-to-(\D+) map:", line):
            changed_within_category = {
                key: False for key in changed_within_category.keys()
            }
            continue
        dst, src, rng = tuple(re.findall(r"(\d+)", line))
        for key, value in seed_map.items():
            if changed_within_category[key]:
                continue
            if value < (int(src) + int(rng)) and value >= int(src):
                offset = value - int(src)
                seed_map[key] = int(dst) + offset
                changed_within_category[key] = True
    return seed_map


def main(file="input.txt"):
    with open(file, "r") as input:
        lines = input.readlines()
    seeds = get_seeds(lines.pop(0))
    seed_map = build_map(seeds, lines)
    seeds_with_ranges = get_seeds_ranges(seeds)
    seed_map_with_ranges = build_map_ranges(seeds_with_ranges, lines)
    return min(seed_map.values()), min([s for (s, _) in seed_map_with_ranges])


def test_part1():
    part1, _ = main("test.txt")
    assert part1 == 35


def test_part2():
    _, part2 = main("test.txt")
    assert part2 == 0  # CHANGE


if __name__ == "__main__":
    part1, part2 = main()
    print(f"The result for part 1 is: {part1}")
    print(f"The result for part 2 is: {part2}")
