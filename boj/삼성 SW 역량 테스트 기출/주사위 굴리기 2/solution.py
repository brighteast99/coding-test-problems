import collections
import sys

VECTORS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def calc_score(n, m, board, x, y):
    stack = [(x, y)]
    visited = set()

    num = board[y][x]
    while len(stack) > 0:
        cur_x, cur_y = stack.pop()

        if (cur_x, cur_y) in visited:
            continue
        visited.add((cur_x, cur_y))

        for dx, dy in VECTORS:
            if not (0 <= cur_x + dx < m and 0 <= cur_y + dy < n):
                continue

            if board[cur_y + dy][cur_x + dx] == num:
                stack.append((cur_x + dx, cur_y + dy))

    return len(visited)


n, m, k = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dice_vertical = collections.deque([2, 1, 5, 6])
dice_horizontal = collections.deque([4, 1, 3, 6])
x, y, direction = 0, 0, 0

score = 0
for _ in range(k):
    dx, dy = VECTORS[direction]

    if not (0 <= x + dx < m and 0 <= y + dy < n):
        direction = (direction + 2) % 4
        dx, dy = VECTORS[direction]

    if direction == 0:
        dice_horizontal.rotate()
    elif direction == 1:
        dice_vertical.rotate()
    elif direction == 2:
        dice_horizontal.rotate(-1)
    else:
        dice_vertical.rotate(-1)

    if direction % 2 == 0:
        dice_vertical[1] = dice_horizontal[1]
        dice_vertical[3] = dice_horizontal[3]
    else:
        dice_horizontal[1] = dice_vertical[1]
        dice_horizontal[3] = dice_vertical[3]

    x += dx
    y += dy
    if dice_horizontal[-1] > board[y][x]:
        direction = (direction + 1) % 4
    elif dice_horizontal[-1] < board[y][x]:
        direction = (direction - 1) % 4

    score += calc_score(n, m, board, x, y) * board[y][x]

print(score)
