import sys
from typing import List

r, c, t = map(int, sys.stdin.readline().split())
room = []
purifier = []

for i in range(r):
    room.append(list(map(int, sys.stdin.readline().split())))
    if room[i][0] == -1:
        purifier.append(i)


def spread(room: List[List[int]]):
    dusts = []

    for y, row in enumerate(room):
        for x, cell in enumerate(row):
            if cell <= 0:
                continue
            dusts.append((x, y, room[y][x]))

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for x, y, dust in dusts:
        spread_amount = dust // 5
        for dx, dy in directions:
            if not (0 <= x + dx < len(room[0]) and 0 <= y + dy < len(room)):
                continue
            if room[y + dy][x + dx] == -1:
                continue

            room[y + dy][x + dx] += spread_amount
            room[y][x] -= spread_amount


def circulate(room: List[List[int]], purifier: List[int]):
    # Upper half
    for i in reversed(range(1, purifier[0])):
        room[i][0] = room[i - 1][0]
    room[0] = [*room[0][1:], room[1][-1]]
    for i in range(1, purifier[0]):
        room[i][-1] = room[i + 1][-1]
    room[purifier[0]] = [-1, 0, *room[purifier[0]][1:-1]]

    # Lower half
    for i in range(purifier[1] + 1, len(room) - 1):
        room[i][0] = room[i + 1][0]
    room[-1] = [*room[-1][1:], room[-2][-1]]
    for i in reversed(range(purifier[1] + 1, len(room))):
        room[i][-1] = room[i - 1][-1]
    room[purifier[1]] = [-1, 0, *room[purifier[1]][1:-1]]


for _ in range(t):
    spread(room)
    circulate(room, purifier)

print(sum(sum(row) for row in room) + 2)
