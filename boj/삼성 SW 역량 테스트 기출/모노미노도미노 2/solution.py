import sys


def shift_down(board, y):
    for cur_y in reversed(range(y)):
        board[cur_y + 1] = board[cur_y]
    board[0] = [False] * 4


def drop_block(board, pos, type):
    blocks = {1: [(0, 0)], 2: [(0, 0), (0, -1)], 3: [(0, 0), (1, 0)]}
    block = blocks[type]

    y = 1 if type == 2 else 0
    while y < 6:
        for dx, dy in block:
            if board[y + dy][pos + dx]:
                break
        else:
            y += 1
            continue
        y -= 1
        break
    else:
        y -= 1

    for dx, dy in block:
        board[y + dy][pos + dx] = True

    score = 0
    for _ in range(2 if type == 2 else 1):
        if all(board[y]):
            score += 1
            shift_down(board, y)
        else:
            y -= 1

    for _ in range(2):
        if any(board[1]):
            shift_down(board, 5)
        else:
            break

    return score


def count_blocks(board):
    return sum(map(lambda row: row.count(True), board))


n = int(sys.stdin.readline())
blue = [[False] * 4 for _ in range(6)]
green = [[False] * 4 for _ in range(6)]

score = 0
for _ in range(n):
    t, x, y = map(int, sys.stdin.readline().split())

    score += drop_block(green, x, t)
    if t == 1:
        score += drop_block(blue, y, t)
    else:
        score += drop_block(blue, y, 2 if t == 3 else 3)
print(score)
print(count_blocks(blue) + count_blocks(green))
