import sys

n = int(sys.stdin.readline())
board = [[-1] * n for _ in range(n)]
board[0][0] = 0

k = int(sys.stdin.readline())
apples = set()
for _ in range(k):
    y, x = map(int, sys.stdin.readline().split())
    apples.add((x - 1, y - 1))

l = int(sys.stdin.readline())
moves = []
for _ in range(l):
    x, c = sys.stdin.readline().split()
    moves.append((int(x), c))
moves.append((10001, ""))

DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
body_len = 1
head, cur_dir = (0, 0), 0
t = 0
for x, c in moves:
    dx, dy = DIRECTIONS[cur_dir]

    for _ in range(t, x):
        t += 1
        x, y = head[0] + dx, head[1] + dy
        if not (0 <= x < n and 0 <= y < n) or (board[y][x] >= t - body_len):
            print(t)
            exit(0)

        board[y][x] = t
        if (x, y) in apples:
            body_len += 1
            apples.remove((x, y))
        head = (x, y)

    if c == "L":
        cur_dir = (cur_dir - 1) % 4
    elif c == "D":
        cur_dir = (cur_dir + 1) % 4
