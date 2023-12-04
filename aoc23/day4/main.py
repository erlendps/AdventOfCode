def get_lines(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    return lines


def task1(filename):
    lines = get_lines(filename)

    points = 0

    for index, line in enumerate(lines):
        num_correct = 0
        line = [l.strip() for l in line.removeprefix(f"Card {index + 1}:").split("|")]
        winning_nums = filter(lambda x: x != "", line[0].split(" "))
        my_nums = filter(lambda x: x != "", line[1].split(" "))
        my_nums_map = dict([(n, n) for n in my_nums])
        for num in winning_nums:
            if num in my_nums_map:
                num_correct += 1
        points += 2 ** (num_correct - 1) if num_correct else 0

    print(points)


def task2(filename):
    lines = get_lines(filename)

    cards_won = dict([(str(i), 1) for i in range(1, len(lines) + 1)])

    for index, line in enumerate(lines):
        num_correct = 0
        line = [l.strip() for l in line.removeprefix(f"Card {index + 1}:").split("|")]
        winning_nums = filter(lambda x: x != "", line[0].split(" "))
        my_nums = filter(lambda x: x != "", line[1].split(" "))
        my_nums_map = dict([(n, n) for n in my_nums])
        for num in winning_nums:
            if num in my_nums_map:
                num_correct += 1

        num_cards = cards_won[str(index + 1)]
        for i in range(1, num_correct + 1):
            cards_won[str(index + 1 + i)] += num_cards

    print("Total number of cards are:", sum(cards_won.values()))


if __name__ == "__main__":
    task1("input.txt")
    task2("input.txt")
