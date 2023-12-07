from solution import main


def test_part1():
    part1, _ = main("test.txt")
    assert part1 == 6440


def test_part2():
    _, part2 = main("test.txt")
    assert part2 == 5905
