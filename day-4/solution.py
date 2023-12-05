import re


def get_card_num(line):
    cardnum = re.findall(r"^Card\s+(\d+):", line)[0]
    return int(cardnum)


def get_num_winning(line):
    split_pattern = re.compile(r"\||:")
    split_line = re.split(split_pattern, line)
    w = split_line[1]
    y = split_line[2]
    nums_pattern = re.compile(r"(\d+)")
    winning = set(re.findall(nums_pattern, w))
    yours = set(re.findall(nums_pattern, y))
    yours_winning = yours & winning
    return len(yours_winning)


def main():
    with open("input.txt", "r") as input:
        lines = input.readlines()
    scores = [
        2 ** (get_num_winning(line) - 1) if get_num_winning(line) != 0 else 0
        for line in lines
    ]
    num_cards = 0
    cards_won = {}
    for card in lines:
        card_num = get_card_num(card)
        num_winning = get_num_winning(card)
        num_this_card = cards_won.get(card_num, 0) + 1
        for i in range(card_num + 1, card_num + num_winning + 1):
            cards_won[i] = cards_won.get(i, 0) + num_this_card
        num_cards += num_this_card
    return sum(scores), num_cards


if __name__ == "__main__":
    part1, part2 = main()
    print(f"The result for part 1 is: {part1}")
    print(f"The result for part 2 is: {part2}")
