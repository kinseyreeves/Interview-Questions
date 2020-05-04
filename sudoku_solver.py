"""
Sudoku solver using back tracking

Kinsey Reeves
"""

import numpy as np


def check_digs(arr):
    # Checks if a flattened array has only digits 1-9
    digs = set([x for x in range(1, 10)])
    if (len(arr) == len(digs) and set(arr) == digs):
        return True
    return False


def check_digs_z(arr, n):
    if n in arr:
        return False
    return True


def check_board(board):
    # Checks if a suduko board is valid
    good = True

    for i in range(len(board)):
        good = good and check_digs(board[:, i])
        good = good and check_digs(board[i, :])
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            good = good and check_digs(np.ndarray.flatten(board[i:i + 3, j:j + 3]))

    return good


def is_possible(board, y, x, n):
    row = board[y, :]
    col = board[:, x]

    rX = (x // 3) * 3
    rY = (y // 3) * 3
    quad = np.ndarray.flatten(board[rY:rY + 3, rX:rX + 3])

    if n in row:
        return False
    elif n in col:
        return False
    elif n in quad:
        return False
    return True


def solve_puzzle():
    global board
    for y in range(0, 9):
        for x in range(0, 9):
            if board[y][x] == 0:
                for n in range(1, 10):
                    if (is_possible(board, y, x, n)):
                        board[y][x] = n
                        solve_puzzle()
                        board[y][x] = 0
                return

    print(board)


def main():
    global board
    print(solve_puzzle())


board = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
         [6, 0, 0, 1, 9, 5, 0, 0, 0],
         [0, 9, 8, 0, 0, 0, 0, 6, 0],
         [8, 0, 0, 0, 6, 0, 0, 0, 3],
         [4, 0, 0, 8, 0, 3, 0, 0, 1],
         [7, 0, 0, 0, 2, 0, 0, 0, 6],
         [0, 6, 0, 0, 0, 0, 2, 8, 0],
         [0, 0, 0, 4, 1, 9, 0, 0, 5],
         [0, 0, 0, 0, 8, 0, 0, 7, 9]]

board = np.asarray(board)

main()
