import sys
from collections import deque

n = int(sys.stdin.readline())
space = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
size = 2
required = size

pos = None
for y in range(n):
    for x in range(n):
        if space[y][x] == 9:
            space[y][x] = 0
            pos = (x, y)
            break
    if pos is not None:
        break


def find_target(n, space, pos, size):
    DIRECTIONS = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    queue = deque([(0, pos)])
    visited = set()

    targets = []
    target_dist = None
    while len(queue) > 0:
        dist, (x, y) = queue.popleft()

        if (x, y) in visited:
            continue
        visited.add((x, y))

        if target_dist is not None and target_dist < dist:
            continue

        if 0 < space[y][x] < size:
            target_dist = dist
            targets.append((x, y))
            continue

        for dx, dy in DIRECTIONS:
            if not (0 <= x + dx < n and 0 <= y + dy < n):
                continue
            if space[y + dy][x + dx] > size:
                continue

            queue.append((dist + 1, (x + dx, y + dy)))

    if target_dist is None:
        return 0, pos

    targets.sort(key=lambda target: (target[1], target[0]))
    return target_dist, targets[0]


time = 0
while True:
    dist, target = find_target(n, space, pos, size)

    if dist == 0:
        break

    time += dist
    pos = target
    space[pos[1]][pos[0]] = 0
    required -= 1
    if required == 0:
        size += 1
        required = size

print(time)
