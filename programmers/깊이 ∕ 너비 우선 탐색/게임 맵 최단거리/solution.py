from collections import deque


def solution(maps):
    n, m = len(maps[0]), len(maps)
    visited = [[False for _ in range(n)] for _ in range(m)]
    DIR_VECTORS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([((0, 0), 1)])

    while len(queue):
        ((x, y), steps) = queue.popleft()

        if x == n - 1 and y == m - 1:
            return steps

        if x not in range(n) or y not in range(m) or visited[y][x] or maps[y][x] == 0:
            continue

        visited[y][x] = True
        queue.extend(((x + dx, y + dy), steps + 1) for (dx, dy) in DIR_VECTORS)

    return -1
