import itertools


def get_lines(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    return lines


FIVE_OF_KIND = 0
FOUR_OF_KIND = 1
FULL_HOUSE = 2
THREE_OF_KIND = 3
TWO_PAIR = 4
ONE_PAIR = 5
HIGH_CARD = 6

hand_type = {
    FIVE_OF_KIND: "Five of a kind",
    FOUR_OF_KIND: "Four of a kind",
    FULL_HOUSE: "Full house",
    THREE_OF_KIND: "Three of a kind",
    TWO_PAIR: "Two pairs",
    ONE_PAIR: "One pair",
    HIGH_CARD: "High card",
}

bigger_than_part1 = {
    "A": ["K", "Q", "J", "T"],
    "K": ["Q", "J", "T"],
    "Q": ["J", "T"],
    "J": ["T"],
    "T": [],
}


def detect_hand_part1(hand):
    cards = {}

    for card in hand:
        if card in cards:
            cards[card] += 1
        else:
            cards[card] = 1

    num_unique_cards = len(cards.keys())
    max_of_one = max(cards.values())

    if num_unique_cards == 1:
        return FIVE_OF_KIND
    elif num_unique_cards == 2:
        return FOUR_OF_KIND if max_of_one == 4 else FULL_HOUSE
    elif num_unique_cards == 3:
        return THREE_OF_KIND if max_of_one == 3 else TWO_PAIR
    elif num_unique_cards == 4:
        return ONE_PAIR
    return HIGH_CARD


def compare_cards_part1(a: str, b: str):
    if a == b:
        return 0

    if a.isnumeric() and b.isnumeric():
        if a > b:
            return 1
        return -1
    elif a.isnumeric() and b.isalpha():
        return -1
    elif a.isalpha() and b.isnumeric():
        return 1
    # both are "letter" cards
    if b in bigger_than_part1[a]:
        return 1
    return -1


def insert_hand_part1(hand_list: list[str], hand: str, bid: int):
    i = 0
    while i < len(hand_list):
        cur_hand = hand_list[i][0]
        for j in range(len(hand)):
            comparison = compare_cards_part1(hand[j], cur_hand[j])
            if comparison == 1:
                hand_list.insert(i, (hand, bid))
                return
            elif comparison == 0:
                continue
            else:
                break
        i += 1
    else:
        hand_list.append((hand, bid))


def task1(filename):
    lines = get_lines(filename)
    rank = len(lines)

    sorted_hands = [[] for _ in range(7)]

    for line in lines:
        hand, bid = line.strip().split()
        bid = int(bid)
        type_of_hand = detect_hand_part1(hand)
        insert_hand_part1(sorted_hands[type_of_hand], hand, bid)

    total = 0
    sorted_hands = list(itertools.chain.from_iterable(sorted_hands))

    for hand in sorted_hands:
        total += hand[1] * rank
        rank -= 1

    print(total)


bigger_than = {
    "A": ["K", "Q", "T"],
    "K": ["Q", "T"],
    "Q": ["T"],
    "T": [],
}


def detect_hand(hand):
    cards = {}

    for card in hand:
        if card in cards:
            cards[card] += 1
        else:
            cards[card] = 1

    if "J" in cards:
        pass

    num_unique_cards = len(cards.keys())
    max_of_one = max(cards.values())

    if num_unique_cards == 1:
        return FIVE_OF_KIND
    elif num_unique_cards == 2:
        if "J" in cards:
            return FIVE_OF_KIND
        return FOUR_OF_KIND if max_of_one == 4 else FULL_HOUSE
    elif num_unique_cards == 3:
        if "J" in cards:
            if cards["J"] > 1:
                return FOUR_OF_KIND
            return FULL_HOUSE if max_of_one == 2 else FOUR_OF_KIND
        return THREE_OF_KIND if max_of_one == 3 else TWO_PAIR
    elif num_unique_cards == 4:
        return THREE_OF_KIND if "J" in cards else ONE_PAIR
    return ONE_PAIR if "J" in cards else HIGH_CARD


def compare_cards(a: str, b: str):
    if a == b:
        return 0

    if a == "J":
        return -1
    elif b == "J":
        return 1

    if a.isnumeric() and b.isnumeric():
        if a > b:
            return 1
        return -1
    elif a.isnumeric() and b.isalpha():
        return -1
    elif a.isalpha() and b.isnumeric():
        return 1
    # both are "letter" cards
    if b in bigger_than[a]:
        return 1
    return -1


def insert_hand(hand_list: list[str], hand: str, bid: int):
    i = 0
    while i < len(hand_list):
        cur_hand = hand_list[i][0]
        for j in range(len(hand)):
            comparison = compare_cards(hand[j], cur_hand[j])
            if comparison == 1:
                hand_list.insert(i, (hand, bid))
                return
            elif comparison == 0:
                continue
            else:
                break
        i += 1
    else:
        hand_list.append((hand, bid))


def task2(filename):
    lines = get_lines(filename)
    rank = len(lines)

    sorted_hands = [[] for _ in range(7)]

    for line in lines:
        hand, bid = line.strip().split()
        bid = int(bid)
        type_of_hand = detect_hand(hand)
        insert_hand(sorted_hands[type_of_hand], hand, bid)

    total = 0
    sorted_hands = list(itertools.chain.from_iterable(sorted_hands))

    for hand in sorted_hands:
        total += hand[1] * rank
        rank -= 1

    print(total)


if __name__ == "__main__":
    task1("input.txt")
    task2("input.txt")
