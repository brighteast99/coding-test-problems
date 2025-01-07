import sys

n, m = map(int, sys.stdin.readline().split())
room = []
cctvs = set()
for y in range(n):
    room.append(list(map(int, sys.stdin.readline().split())))
    for x, cell in enumerate(room[-1]):
        if 0 < cell < 6:
            cctvs.add((cell, x, y))

directions = {
    1: [[(1, 0)], [(-1, 0)], [(0, 1)], [(0, -1)]],
    2: [[(1, 0), (-1, 0)], [(0, 1), (0, -1)]],
    3: [[(1, 0), (0, -1)], [(1, 0), (0, 1)], [(-1, 0), (0, -1)], [(-1, 0), (0, 1)]],
    4: [
        [(1, 0), (-1, 0), (0, 1)],
        [(1, 0), (-1, 0), (0, -1)],
        [(1, 0), (0, 1), (0, -1)],
        [(0, 1), (0, -1), (-1, 0)],
    ],
    5: [[(1, 0), (-1, 0), (0, 1), (0, -1)]],
}


def mark_range(room, n, m, x, y, directions):
    for dx, dy in directions:
        dist = 1
        while 0 <= x + dx * dist < m and 0 <= y + dy * dist < n:
            cur_x, cur_y = x + dx * dist, y + dy * dist
            if room[cur_y][cur_x] == 6:
                break
            if room[cur_y][cur_x] == 0:
                room[cur_y][cur_x] = "#"
            dist += 1


def dfs(room, n, m, cctvs):
    if len(cctvs) == 0:
        return sum(row.count(0) for row in room)

    typ, x, y = cctvs[0]
    answer = m * n
    for dirs in directions[typ]:
        new_room = [row.copy() for row in room]
        mark_range(new_room, n, m, x, y, dirs)
        answer = min(answer, dfs(new_room, n, m, cctvs[1:]))

    return answer


print(dfs(room, n, m, list(cctvs)))
