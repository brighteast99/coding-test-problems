import sys

RIGHT, LEFT, UP, DOWN = 1, 2, 3, 4

R, C, K = map(int, sys.stdin.readline().split())
room = [[0] * C for _ in range(R)]
heaters = set()
walls = set()
targets = set()

for y in range(R):
    row = map(int, sys.stdin.readline().split())
    for x, value in enumerate(row):
        if value == 0:
            continue
        elif value == 5:
            targets.add((x, y))
        else:
            heaters.add((x, y, value))

w = int(sys.stdin.readline())
for _ in range(w):
    r, c, t = map(int, sys.stdin.readline().split())
    if t == 0:
        walls.add((c - 1, r - 1, UP))
        walls.add((c - 1, r - 2, DOWN))
    else:
        walls.add((c - 1, r - 1, RIGHT))
        walls.add((c, r - 1, LEFT))


def heat(x, y, direction_info):
    WIND_DIRECTIONS = {
        RIGHT: [
            {"dest": (1, -1), "conditions": [(0, -1, RIGHT), (0, -1, DOWN)]},
            {"dest": (1, 0), "conditions": [(0, 0, RIGHT)]},
            {"dest": (1, 1), "conditions": [(0, 1, RIGHT), (0, 1, UP)]},
        ],
        LEFT: [
            {"dest": (-1, -1), "conditions": [(0, -1, LEFT), (0, -1, DOWN)]},
            {"dest": (-1, 0), "conditions": [(0, 0, LEFT)]},
            {"dest": (-1, 1), "conditions": [(0, 1, LEFT), (0, 1, UP)]},
        ],
        UP: [
            {"dest": (-1, -1), "conditions": [(-1, 0, UP), (-1, 0, RIGHT)]},
            {"dest": (0, -1), "conditions": [(0, 0, UP)]},
            {"dest": (1, -1), "conditions": [(1, 0, UP), (1, 0, LEFT)]},
        ],
        DOWN: [
            {"dest": (-1, 1), "conditions": [(-1, 0, DOWN), (-1, 0, RIGHT)]},
            {"dest": (0, 1), "conditions": [(0, 0, DOWN)]},
            {"dest": (1, 1), "conditions": [(1, 0, DOWN), (1, 0, LEFT)]},
        ],
    }
    wind_directions = WIND_DIRECTIONS[direction_info]
    winds = set(
        [(x + wind_directions[1]["dest"][0], y + wind_directions[1]["dest"][1])]
    )
    for temperature in reversed(range(1, 6)):
        new_winds = set()
        for wind_x, wind_y in winds:
            room[wind_y][wind_x] += temperature
            for direction_info in wind_directions:
                dx, dy = direction_info["dest"]
                next_x, next_y = wind_x + dx, wind_y + dy
                if not (0 <= next_x < C and 0 <= next_y < R):
                    continue

                for wall_x, wall_y, wall_direction in direction_info["conditions"]:
                    if (wind_x + wall_x, wind_y + wall_y, wall_direction) in walls:
                        break
                else:
                    new_winds.add((next_x, next_y))
        winds = new_winds


def convect():
    new_room = [[0] * C for _ in range(R)]

    VECTORS = {RIGHT: (1, 0), LEFT: (-1, 0), UP: (0, -1), DOWN: (0, 1)}

    for y in range(R):
        for x in range(C):
            if room[y][x] == 0:
                continue

            heat_loss = 0
            for direction, (dx, dy) in VECTORS.items():
                if (x, y, direction) in walls:
                    continue
                if not (0 <= x + dx < C and 0 <= y + dy < R):
                    continue
                diff = room[y][x] - room[y + dy][x + dx]
                if diff <= 0:
                    continue

                heat_loss += diff // 4
                new_room[y + dy][x + dx] += diff // 4
            new_room[y][x] += room[y][x] - heat_loss
    return new_room


def cool_down():
    for x in range(C):
        room[0][x] = max(0, room[0][x] - 1)
        room[R - 1][x] = max(0, room[R - 1][x] - 1)
    for y in range(1, R - 1):
        room[y][0] = max(0, room[y][0] - 1)
        room[y][C - 1] = max(0, room[y][C - 1] - 1)


chocolates = 0
while chocolates <= 100:
    for x, y, direction in heaters:
        heat(x, y, direction)

    room = convect()

    cool_down()

    chocolates += 1

    if all(room[y][x] >= K for (x, y) in targets):
        break

print(chocolates)
