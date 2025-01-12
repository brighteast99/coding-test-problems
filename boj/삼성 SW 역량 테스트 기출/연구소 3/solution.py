import sys
from collections import deque
from itertools import combinations

ADJACENT_VECTORS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def expand(n, lab, viruses):
    queue = deque(map(lambda virus: (*virus, 0), viruses))
    visited = set()

    max_time = 0
    expandable = [[lab[y][x] > 0 for x in range(n)] for y in range(n)]
    while len(queue) > 0:
        x, y, time = queue.popleft()

        if (x, y) in visited:
            continue
        visited.add((x, y))
        if lab[y][x] == 0:
            max_time = max(max_time, time)
        expandable[y][x] = True

        for dx, dy in ADJACENT_VECTORS:
            if not (0 <= x + dx < n and 0 <= y + dy < n):
                continue

            if lab[y + dy][x + dx] == 1:
                continue

            queue.append((x + dx, y + dy, time + 1))

    if not all(sum(expandable, [])):
        return -1
    return max_time


n, m = map(int, sys.stdin.readline().split())
lab = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
viruses = set()

for y in range(n):
    for x in range(n):
        if lab[y][x] == 2:
            viruses.add((x, y))

min_time = -1
for activated in combinations(viruses, m):
    time = expand(n, lab, activated)
    if time != -1:
        min_time = min(min_time, time) if min_time > 0 else time
print(min_time)
