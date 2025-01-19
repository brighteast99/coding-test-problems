import sys

RIGHT, DOWN, LEFT, UP = 0, 1, 2, 3
VECTORS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def move(n, board, direction):
    board = [row.copy() for row in board]

    sequence = None
    if direction == UP:
        sequence = [(x, y) for y in range(n) for x in range(n)]
    elif direction == DOWN:
        sequence = [(x, y) for y in reversed(range(n)) for x in range(n)]
    elif direction == LEFT:
        sequence = [(x, y) for x in range(n) for y in range(n)]
    elif direction == RIGHT:
        sequence = [(x, y) for x in reversed(range(n)) for y in range(n)]

    dx, dy = VECTORS[direction]
    merged = set()
    for x, y in sequence:
        if board[y][x] == 0:
            continue

        cur_x, cur_y = x, y
        while (0 <= cur_x + dx < n and 0 <= cur_y + dy < n) and (
            board[cur_y + dy][cur_x + dx] == 0
            or (
                (cur_x + dx, cur_y + dy) not in merged
                and board[cur_y + dy][cur_x + dx] == board[y][x]
            )
        ):
            cur_x, cur_y = cur_x + dx, cur_y + dy

        if (cur_x, cur_y) == (x, y):
            continue

        if board[cur_y][cur_x] == board[y][x]:
            board[cur_y][cur_x] = board[y][x] * 2
            merged.add((cur_x, cur_y))
        else:
            board[cur_y][cur_x] = board[y][x]
        board[y][x] = 0

    return board


def dfs(n, board, moves=0, direction=None):
    if direction is not None:
        moves += 1
        board = move(n, board, direction)

    if moves == 5:
        return max(map(max, board))

    max_num = 0
    for direction in range(4):
        max_num = max(max_num, dfs(n, board, moves, direction))

    return max_num


n = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

print(dfs(n, board))
