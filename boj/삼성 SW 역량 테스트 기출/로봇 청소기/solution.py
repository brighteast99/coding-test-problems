import sys

n, m = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())
floor = [list(map(int, line.split())) for line in sys.stdin.readlines()]
DIRTY, WALL, CLEANED = 0, 1, 2
DIRECTIONS = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # NESW


cleaned = 0
while True:
    if floor[r][c] == DIRTY:
        floor[r][c] = CLEANED
        cleaned += 1

    for dx, dy in DIRECTIONS:
        if floor[r + dy][c + dx] == DIRTY:
            break
    else:
        dx, dy = DIRECTIONS[(d + 2) % 4]  # backward
        if floor[r + dy][c + dx] == WALL:
            break
        c, r = c + dx, r + dy
        continue

    for i, (dx, dy) in enumerate(DIRECTIONS[d - 1 :: -1] + DIRECTIONS[: d - 1 : -1]):
        if floor[r + dy][c + dx] == DIRTY:
            c, r = c + dx, r + dy
            d = (d - (i + 1)) % 4
            break

print(cleaned)
