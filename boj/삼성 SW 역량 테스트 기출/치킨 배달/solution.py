import itertools
import sys

n, m = map(int, sys.stdin.readline().split())

homes, chickens = [], []
for y in range(n):
    row = map(int, sys.stdin.readline().split())
    for x, cell in enumerate(row):
        if cell == 1:
            homes.append((x, y))
        elif cell == 2:
            chickens.append((x, y))

answer = 4 * n**2
for pruned_chickens in itertools.combinations(chickens, m):
    local_answer = 0
    for x, y in homes:
        dist = 2 * n
        for chicken_x, chicken_y in pruned_chickens:
            dist = min(dist, abs(x - chicken_x) + abs(y - chicken_y))
        local_answer += dist
    answer = min(answer, local_answer)

print(answer)
