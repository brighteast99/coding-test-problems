from collections import deque


def solution(rectangle, characterX, characterY, itemX, itemY):
    plane = [[False for _ in range(102)] for _ in range(102)]
    visited = [[False for _ in range(101)] for _ in range(101)]
    check_vectors = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]
    move_vectors = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for [lbx, lby, rtx, rty] in rectangle:
        for y in range(lby * 2, rty * 2 + 1):
            for x in range(lbx * 2, rtx * 2 + 1):
                plane[y][x] = True
    queue = deque([((characterX * 2, characterY * 2), 0)])

    while len(queue) > 0:
        (x, y), steps = queue.popleft()

        if all(plane[y + dy][x + dx] for (dx, dy) in check_vectors):
            continue

        if visited[y][x]:
            continue

        if x == itemX * 2 and y == itemY * 2:
            return steps // 2

        visited[y][x] = True
        queue.extend(
            ((x + dx, y + dy), steps + 1)
            for (dx, dy) in move_vectors
            if plane[y + dy][x + dx]
        )

    return -1
