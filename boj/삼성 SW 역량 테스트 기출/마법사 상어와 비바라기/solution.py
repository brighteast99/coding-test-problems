import sys

n, m = map(int, sys.stdin.readline().split())
baskets = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

DIRECTIONS = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
DIAGONALS = [(-1, -1), (-1, 1), (1, 1), (1, -1)]

clouds = {(n - 1, 0), (n - 1, 1), (n - 2, 0), (n - 2, 1)}
for _ in range(m):
    d, s = map(int, sys.stdin.readline().split())
    dy, dx = DIRECTIONS[d - 1]
    clouds = {((y + dy * s) % n, (x + dx * s) % n) for (y, x) in clouds}

    for y, x in clouds:
        baskets[y][x] += 1

    for y, x in clouds:
        for dy, dx in DIAGONALS:
            if not (0 <= y + dy < n and 0 <= x + dx < n):
                continue
            if baskets[y + dy][x + dx] > 0:
                baskets[y][x] += 1

    new_clouds = set()
    for y in range(n):
        for x in range(n):
            if baskets[y][x] < 2 or (y, x) in clouds:
                continue
            baskets[y][x] -= 2
            new_clouds.add((y, x))

    clouds = new_clouds


print(sum(sum(row) for row in baskets))
