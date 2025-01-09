import sys
from collections import deque

n, m, k = map(int, sys.stdin.readline().split())
earth = [[5] * n for _ in range(n)]
a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
trees = [[deque() for _ in range(n)] for _ in range(n)]

for _ in range(m):
    r, c, age = map(int, sys.stdin.readline().split())
    trees[r - 1][c - 1].append(age)

DIRECTIONS = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
for _ in range(k):
    to_spread = []
    for r in range(n):
        for c in range(n):
            fertilizer = 0
            for _ in range(len(trees[r][c])):
                age = trees[r][c].popleft()

                # spring
                if earth[r][c] >= age:
                    earth[r][c] -= age
                    age += 1
                    trees[r][c].append(age)
                    if age % 5 == 0:
                        for dr, dc in DIRECTIONS:
                            if not (0 <= r + dr < n and 0 <= c + dc < n):
                                continue
                            to_spread.append((r + dr, c + dc))
                else:
                    # summer(accum)
                    fertilizer += age // 2

            # summer(add)
            earth[r][c] += fertilizer
            # winter
            earth[r][c] += a[r][c]

    # fall
    for r, c in to_spread:
        trees[r][c].appendleft(1)

n_trees = 0
for r in range(n):
    for c in range(n):
        n_trees += len(trees[r][c])

print(n_trees)
