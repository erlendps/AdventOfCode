occupied = {}

max_y = 0


def get_move(x, y):
    if (x, y + 1) not in occupied:
        return (x, y + 1)
    elif (x - 1, y + 1) not in occupied:
        return (x - 1, y + 1)
    elif (x + 1, y + 1) not in occupied:
        return (x + 1, y + 1)
    else:
        return 0


def draw_line(first, next):
    global occupied
    occupied[first] = "#"
    if first[0] == next[0]:
        for i in range(1, next[1] - first[1] + 1):
            occupied[(first[0], first[1] + i)] = "#"
    else:
        for i in range(1, next[0] - first[0] + 1):
            occupied[(first[0] + i, first[1])] = "#"


def get_limits(points):
    return (
        min([p[0] for p in points]),
        max([p[0] for p in points]),
        min([p[1] for p in points]),
        max([p[1] for p in points]),
    )


with open("input.txt", "r") as f:
    for line in f.readlines():
        path = line.split("->")
        for i, point in enumerate(path):
            path[i] = eval("(" + point.strip() + ")")
        for start, end in zip(path[:-1], path[1:]):
            min_x, max_x, min_y, max_y = get_limits([start, end])
            for x in range(min_x, max_x + 1):
                for y in range(min_y, max_y + 1):
                    occupied[(x, y)] = "#"

num_rocks = len(occupied)
# start simulating
position = (500, 0)
y_max = get_limits(occupied.keys())[-1]
while True:
    move = get_move(position[0], position[1])
    if move == 0:
        occupied[position] = "s"
        position = (500, 0)
    elif move[1] == max_y:
        print(move)
        break
    else:
        position = move

print(len([i for i in occupied.values() if i == "s"]))
