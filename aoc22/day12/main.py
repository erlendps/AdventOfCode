from typing import List


class PriQ:
    def __init__(self, f: List[List[int]]) -> None:
        self.queue: List[tuple] = []
        self.f = f

    def insert(self, point: tuple):
        self.queue.append(point)
        self.resort()

    def resort(self):
        self.queue.sort(key=(lambda x: self.f[x[0]][x[1]]))

    def pop(self):
        return self.queue.pop(0)

    def isEmpty(self):
        return len(self.queue) == 0

    def contains(self, point):
        return point in self.queue

    def __str__(self) -> str:
        return str(self.queue)


grid = []
# 0: row 1: col
start = []
possible_starts = []
goal = []


with open("input.txt", "r") as f:
    for row, line in enumerate(f.readlines()):
        line = line.strip()
        grid.append(line)
        for col, char in enumerate(line):
            if char == "S":
                start = (row, col)
                possible_starts.append((row, col))
                line = line.replace("S", "a")
                grid[row] = line
            if char == "E":
                goal = (row, col)
                line = line.replace("E", "z")
                grid[row] = line
            if char == "a":
                possible_starts.append((row, col))


def backtrack(came_from: dict[tuple, tuple], current):
    path = [current]

    while current in came_from.keys():
        current = came_from[current]
        path.insert(0, current)
    return path


def a_star(grid, start, goal):
    max_x = len(grid[0])
    max_y = len(grid)
    came_from = {}

    def get_neighbors(point: tuple) -> List[tuple]:
        neighbors = []
        if point[0] - 1 >= 0:
            neighbors.append((point[0] - 1, point[1]))
        if point[0] + 1 < max_y:
            neighbors.append((point[0] + 1, point[1]))
        if point[1] - 1 >= 0:
            neighbors.append((point[0], point[1] - 1))
        if point[1] + 1 < max_x:
            neighbors.append((point[0], point[1] + 1))
        return neighbors

    def h(point: tuple[int]):
        return abs(goal[1] - point[0]) + abs(goal[0] - point[0])

    f = [[float("inf") for _ in range(max_x)] for _ in range(max_y)]
    g = [[float("inf") for _ in range(max_x)] for _ in range(max_y)]
    f[start[0]][start[1]] = h(start)
    g[start[0]][start[1]] = 0
    d = 1

    q = PriQ(f)
    q.insert(start)

    while not q.isEmpty():
        current = q.pop()
        if current == goal:
            return backtrack(came_from, current)

        for neighbor in get_neighbors(current):
            if ord(grid[neighbor[0]][neighbor[1]]) - ord(grid[current[0]][current[1]]) > 1:
                continue
            tent_g_score = g[current[0]][current[1]] + d
            if tent_g_score < g[neighbor[0]][neighbor[1]]:
                came_from[neighbor] = current
                g[neighbor[0]][neighbor[1]] = tent_g_score
                f[neighbor[0]][neighbor[1]] = tent_g_score + h(neighbor)
                if not q.contains(neighbor):
                    q.insert(neighbor)
                else:
                    q.resort()
    return []


# part 1
sol = a_star(grid, start, goal)
print("Number of steps:", len(sol) - 1)

# part 2
current_best = float("inf")
for s in possible_starts:
    length = len(a_star(grid, s, goal)) - 1
    if length == -1:
        continue
    if length < current_best:
        current_best = length

print("Best trip:", current_best)
