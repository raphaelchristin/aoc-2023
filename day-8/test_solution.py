from solution import main


def test_part1():
    part1, _ = main("test.txt")
    assert part1 == 2


def test2_part1():
    part1, _ = main("test2.txt")
    assert part1 == 6


def test_part2():
    _, part2 = main("test3.txt")
    assert part2 == 6
