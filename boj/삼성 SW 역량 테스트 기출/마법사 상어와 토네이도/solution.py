import sys


def rotate(vector, direction):
    COS = [1, 0, -1, 0]
    SIN = [0, 1, 0, -1]
    x, y = vector

    x, y = (
        x * COS[direction] - y * SIN[direction],
        -(x * SIN[direction] + y * COS[direction]),
    )

    return x, y


def spread(n, board, x, y, direction):
    spread = [
        (1, -1, 0.01),
        (1, 1, 0.01),
        (0, -1, 0.07),
        (0, -2, 0.02),
        (0, 1, 0.07),
        (0, 2, 0.02),
        (-1, -1, 0.1),
        (-2, 0, 0.05),
        (-1, 1, 0.1),
    ]

    initial_sand = board[y][x]
    blown_out = 0
    for dx, dy, r in spread:
        dx, dy = rotate((dx, dy), direction)
        blown = int(initial_sand * r)
        board[y][x] -= blown
        if not (0 <= x + dx < n and 0 <= y + dy < n):
            blown_out += blown
        else:
            board[y + dy][x + dx] += blown

    dx, dy = rotate((-1, 0), direction)
    if not (0 <= x + dx < n and 0 <= y + dy < n):
        blown_out += board[y][x]
    else:
        board[y + dy][x + dx] += board[y][x]
    board[y][x] = 0

    return blown_out


n = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]


directions = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}
moves = zip(
    sum([[i] * 2 for i in range(1, n)], []) + [n - 1], [i % 4 for i in range(2 * n - 1)]
)
pos = (n // 2, n // 2)
answer = 0
while pos != (0, 0):
    for dist, direction in moves:
        dx, dy = directions[direction]
        for _ in range(dist):
            pos = (pos[0] + dx, pos[1] + dy)
            answer += spread(n, board, pos[0], pos[1], direction)
print(answer)
