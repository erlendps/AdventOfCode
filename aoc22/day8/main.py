import numpy as np

grid = []
num_invisible = 0

with open("input.txt", "r") as f:
    for line in f.readlines():
        line = [int(i) for i in line.strip()]
        grid.append(line)

# Part 1
num_tiles = len(grid) * len(grid[0])
grid_size = len(grid)
for j in range(1, grid_size - 1):
    for i in range(1, len(grid[j]) - 1):
        curr_el = grid[j][i]
        max_up = max([grid[x][i] for x in range(j)])
        max_right = max(grid[j][i+1:])
        max_down = max([grid[x][i] for x in range(j+1, grid_size)])
        max_left = max(grid[j][:i])
        if curr_el <= max_up and curr_el <= max_right \
                and curr_el <= max_down and curr_el <= max_left:
            num_invisible += 1

print(num_tiles - num_invisible)

# part 2 dont consider edges since they give a factor of 0

max_score = 0
for j in range(1, grid_size - 1):
    for i in range(1, len(grid[j]) - 1):
        tile_score = 1
        curr_el = grid[j][i]
        index_up = np.where(np.array([grid[x][i]
                            for x in range(j-1, -1, -1)]) >= curr_el)[0]
        if len(index_up) == 0:
            tile_score *= j
        else:
            tile_score *= index_up[0] + 1

        index_left = np.where(np.array(grid[j][:i][::-1]) >= curr_el)[0]
        if len(index_left) == 0:
            tile_score *= i
        else:
            tile_score *= index_left[0] + 1

        index_right = np.where(np.array(grid[j][i+1:]) >= curr_el)[0]
        if len(index_right) == 0:
            tile_score *= grid_size - i - 1
        else:
            tile_score *= index_right[0] + 1

        index_down = np.where(np.array([grid[x][i]
                                        for x in range(j+1, grid_size)]) >= curr_el)[0]
        if len(index_down) == 0:
            tile_score *= grid_size - j - 1
        else:
            tile_score *= index_down[0] + 1

        if (tile_score > max_score):
            max_score = tile_score

print(max_score)
