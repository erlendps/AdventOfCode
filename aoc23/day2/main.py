from functools import reduce


def get_lines(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    return lines


def task1(filename):
    lines = get_lines(filename)

    limits = {"red": 12, "green": 13, "blue": 14}
    id_sum = 0
    for line in lines:
        line = line.removeprefix("Game ").strip().replace(",", "")
        line = line.split(":")
        current_id = int(line[0])
        game = line[1].split(";")
        valid = True
        for grab in game:
            current_count = {"red": 0, "green": 0, "blue": 0}
            grab = grab.strip().split(" ")
            for count, color in zip(grab[0::2], grab[1::2]):
                current_count[color] += int(count)
            if any(current_count[col] > limits[col] for col in limits.keys()):
                valid = False
                break
        if valid:
            id_sum += current_id
    print("Total sum of ids:", id_sum)


def task2(filename):
    lines = get_lines(filename)

    power_sum = 0

    for line in lines:
        line = line.removeprefix("Game ").strip().replace(",", "")
        game = line.split(":")[1].split(";")
        min_count = {"red": 0, "green": 0, "blue": 0}
        for grab in game:
            current_count = {"red": 0, "green": 0, "blue": 0}
            grab = grab.strip().split(" ")
            for count, color in zip(grab[0::2], grab[1::2]):
                current_count[color] += int(count)
            for color in min_count.keys():
                if (count := current_count[color]) > min_count[color]:
                    min_count[color] = count
        power_sum += reduce((lambda x, y: x * y), min_count.values())

    print("The power sum is:", power_sum)


if __name__ == "__main__":
    # task1("input.txt")
    task2("input.txt")
