import sys

DIRECTION_VECTORS = [(0, -1), (0, 1), (-1, 0), (1, 0)]


n, m, k = map(int, sys.stdin.readline().split())
sharks = {shark: None for shark in range(1, m + 1)}
prefs = {shark: None for shark in range(1, m + 1)}
board = [[] for _ in range(n)]

for y in range(n):
    for x, cell in enumerate(sys.stdin.readline().split()):
        cell = int(cell)
        if cell != 0:
            sharks[cell] = (x, y)
            board[y].append((cell, k))
        else:
            board[y].append(None)

for shark, direction in enumerate(map(int, sys.stdin.readline().split())):
    sharks[shark + 1] = (sharks[shark + 1], direction - 1)

for shark in range(1, m + 1):
    prefs[shark] = {}
    for direction in range(4):
        prefs[shark][direction] = list(
            map(lambda direction: int(direction) - 1, sys.stdin.readline().split())
        )


time = 0
while time < 1000:
    time += 1

    next_pos = {}
    for shark in reversed(range(1, m + 1)):
        if sharks[shark] is None:
            continue

        (cur_x, cur_y), cur_direction = sharks[shark]
        for new_direction in prefs[shark][cur_direction]:
            dx, dy = DIRECTION_VECTORS[new_direction]
            new_x, new_y = cur_x + dx, cur_y + dy

            if not (0 <= new_x < n and 0 <= new_y < n):
                continue

            if board[new_y][new_x] is None:
                next_pos[shark] = ((new_x, new_y), new_direction)
                break
        else:
            for new_direction in prefs[shark][cur_direction]:
                dx, dy = DIRECTION_VECTORS[new_direction]
                new_x, new_y = cur_x + dx, cur_y + dy

                if not (0 <= new_x < n and 0 <= new_y < n):
                    continue

                another_shark, smell_left = board[new_y][new_x]
                if another_shark == shark:
                    next_pos[shark] = ((new_x, new_y), new_direction)
                    break

    for shark in reversed(range(1, m + 1)):
        if shark not in next_pos:
            continue
        sharks[shark] = next_pos[shark]
        (x, y), _ = sharks[shark]
        if board[y][x] is not None:
            another_shark, smell_left = board[y][x]
            if another_shark != shark and smell_left == k + 1:
                sharks[another_shark] = None
        board[y][x] = (shark, k + 1)

    for y in range(n):
        for x in range(n):
            if board[y][x] is None:
                continue
            shark, smell_left = board[y][x]
            if smell_left == 1:
                board[y][x] = None
            else:
                board[y][x] = (shark, smell_left - 1)

    for shark in range(2, m + 1):
        if sharks[shark] is not None:
            break
    else:
        break
else:
    time = -1
print(time)
