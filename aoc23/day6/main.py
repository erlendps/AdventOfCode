def get_lines(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    return lines


def task1(filename):
    times, distances = [line.split(":")[1].strip() for line in get_lines(filename)]

    times = list(map(int, times.split()))
    distances = list(map(int, distances.split()))

    ways = 1

    for t, d in zip(times, distances):
        # no point calculating for time pressed = 0 or = t
        for t_p in range(t // 2):
            t_r = t - t_p
            # t_p is the speed it gets, t_r is traveling time
            if t_p * t_r > d:
                break

        ways *= t - 2 * t_p + 1

    print(ways)


def task2(filename):
    time, distance = [line.split(":")[1].strip() for line in get_lines(filename)]

    time = int("".join(list(map(str, map(int, time.split())))))
    distance = int("".join(list(map(str, map(int, distance.split())))))

    for t_p in range(time):
        t_r = time - t_p
        # t_p is the speed it gets, t_r is traveling time
        if t_p * t_r > distance:
            break

    ways_to_win = time - 2 * t_p + 1
    print(ways_to_win)


if __name__ == "__main__":
    task1("input.txt")
    task2("input.txt")
