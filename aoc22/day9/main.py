# y grows downwards, x towards right
sign_map = {"U": -1, "R": 1, "D": 1, "L": -1}

head = [0, 0]
tails = [[0, 0] for _ in range(9)]
tail_visited = set([])


def is_neighbor(head, tail):
    return abs(head[0] - tail[0]) <= 1 and abs(head[1] - tail[1]) <= 1


def update_tail():
    curr_head = head
    for i in range(len(tails)):
        curr_tail = tails[i]
        if not is_neighbor(curr_head, curr_tail):
            if (diff_col := curr_head[0] - curr_tail[0]) != 0:
                if diff_col < 0:
                    curr_tail[0] -= 1
                else:
                    curr_tail[0] += 1
            if (diff_row := curr_head[1] - curr_tail[1]) != 0:
                if diff_row < 0:
                    curr_tail[1] -= 1
                else:
                    curr_tail[1] += 1

        curr_head = tails[i]


with open("input.txt", "r") as f:
    for line in f.readlines():
        line = line.strip().split(" ")
        sign = sign_map[line[0]]
        orientation = 0  # move along row
        if line[0] == "U" or line[0] == "D":
            orientation = 1  # move along column

        for _ in range(int(line[1])):
            head[orientation] += sign
            update_tail()
            tail_visited.add(tuple(tails[-1]))


print(len(tail_visited))
