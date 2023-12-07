from functools import cmp_to_key


def get_hand_score(hand, joker=False):
    cards = {}
    for c in hand:
        cards[c] = cards.get(c, 0) + 1
    if joker:
        n_joker = cards.pop("J", 0)
        if not cards:
            return 7
        max_card = max(cards, key=lambda x: cards[x])
        cards[max_card] += n_joker
    score = 8 - len(cards)
    if len(cards) >= 2:
        score -= 1
    if len(cards) >= 3:
        score -= 1
    if len(cards) in [2, 3] and 5 - len(cards) < max(cards.values()):
        score += 1
    return score


def compare_char(c1, c2, joker=False):
    suit_scores = {
        "A": "14",
        "K": "13",
        "Q": "12",
        "J": "11",
        "T": "10",
    }
    if joker:
        suit_scores.update({"J": "0"})
    c1 = suit_scores.get(c1) or c1
    c2 = suit_scores.get(c2) or c2
    c1, c2 = map(int, [c1, c2])
    if c1 > c2:
        return 1
    return -1


def compare_hands(hand_1, hand_2, joker=False):
    score_1, score_2 = [get_hand_score(h, joker) for h in [hand_1[0], hand_2[0]]]
    if score_1 > score_2:
        return 1
    if score_1 == score_2:
        for c1, c2 in zip(hand_1[0], hand_2[0]):
            if c1 == c2:
                continue
            return compare_char(c1, c2, joker)
    return -1


def compare_hands_j(hand_1, hand_2):
    return compare_hands(hand_1, hand_2, True)


def argsort(seq, cmp=compare_hands):
    return [
        idx
        for _, idx in sorted([(v, i) for (i, v) in enumerate(seq)], key=cmp_to_key(cmp))
    ]


def main(file="input.txt"):
    with open(file, "r") as input:
        lines = input.readlines()
    lines = [line.split() for line in lines]
    hands = [line[0] for line in lines]
    bets = [int(line[1]) for line in lines]
    order = argsort(hands)
    order_joker = argsort(hands, compare_hands_j)
    winnings = [bets[o] * (i + 1) for i, o in enumerate(order)]
    winnings_joker = [bets[o] * (i + 1) for i, o in enumerate(order_joker)]
    return sum(winnings), sum(winnings_joker)


if __name__ == "__main__":
    part1, part2 = main()
    print(f"The result for part 1 is: {part1}")
    print(f"The result for part 2 is: {part2}")
