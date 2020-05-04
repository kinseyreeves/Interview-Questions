import numpy as np


def grid_search(n):
    grid = np.zeros(shape=(n + 1, n + 1))
    for i in range(0, n):
        grid[n, i] = 1
        grid[i, n] = 1

    for i in range(n - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            grid[i][j] = grid[i + 1][j] + grid[i][j + 1]

    print(grid)
    print(grid[0][0])


grid_search(20)

# n^2+(n-1)^2
# 1 : 2
# 2 : 6
# 3 : 20
