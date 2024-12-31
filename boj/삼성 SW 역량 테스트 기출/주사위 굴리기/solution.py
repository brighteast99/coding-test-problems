import collections
import sys

n, m, y, x, k = map(int, sys.stdin.readline().split())

board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))

dice_vertical = collections.deque([0, 0, 0, 0])
dice_horizontal = collections.deque([0, 0, 0, 0])
VECTORS = [(1, 0), (-1, 0), (0, -1), (0, 1)]
for move in map(int, sys.stdin.readline().split()):
    dx, dy = VECTORS[move - 1]

    if not (0 <= x + dx < m and 0 <= y + dy < n):
        continue

    x += dx
    y += dy

    if move == 1:
        dice_horizontal.rotate()
        dice_vertical[1] = dice_horizontal[1]
        dice_vertical[3] = dice_horizontal[3]
    elif move == 2:
        dice_horizontal.rotate(-1)
        dice_vertical[1] = dice_horizontal[1]
        dice_vertical[3] = dice_horizontal[3]
    elif move == 3:
        dice_vertical.rotate()
        dice_horizontal[1] = dice_vertical[1]
        dice_horizontal[3] = dice_vertical[3]
    else:
        dice_vertical.rotate(-1)
        dice_horizontal[1] = dice_vertical[1]
        dice_horizontal[3] = dice_vertical[3]

    if board[y][x] == 0:
        board[y][x] = dice_vertical[3]
    else:
        dice_vertical[3] = board[y][x]
        dice_horizontal[3] = board[y][x]
        board[y][x] = 0

    print(dice_horizontal[1])
