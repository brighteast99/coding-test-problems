import sys


def move(c, r, x, y, distance, direction):
    UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3

    if direction == UP:
        if distance <= y:
            return (x, y - distance, UP)
        elif distance <= y + r - 1:
            return (x, distance - y, DOWN)
        else:
            return (x, 2 * (r - 1) - distance + y, UP)
    elif direction == RIGHT:
        if distance <= c - 1 - x:
            return (x + distance, y, RIGHT)
        elif distance <= 2 * (c - 1) - x:
            return (2 * (c - 1) - x - distance, y, LEFT)
        else:
            return (distance - 2 * (c - 1) + x, y, RIGHT)
    elif direction == DOWN:
        if distance <= r - 1 - y:
            return (x, y + distance, DOWN)
        elif distance <= 2 * (r - 1) - y:
            return (x, 2 * (r - 1) - y - distance, UP)
        else:
            return (x, distance - 2 * (r - 1) + y, DOWN)
    elif direction == LEFT:
        if distance <= x:
            return (x - distance, y, LEFT)
        elif distance <= x + c - 1:
            return (distance - x, y, RIGHT)
        else:
            return (2 * (c - 1) - distance + x, y, LEFT)


r, c, m = map(int, sys.stdin.readline().split())
board = [[None for _ in range(c)] for _ in range(r)]
sharks = {}

for _ in range(m):
    y, x, s, d, z = map(int, sys.stdin.readline().split())
    d -= 1
    if d == 1:
        d = 2
    elif d == 2:
        d = 1

    if d % 2 == 0:
        s %= (r - 1) * 2
    else:
        s %= (c - 1) * 2
    board[y - 1][x - 1] = z
    sharks[z] = ((x - 1, y - 1), s, d)


answer = 0
for fisher in range(c):
    for y in range(r):
        if board[y][fisher] is None:
            continue
        size = board[y][fisher]
        answer += size
        board[y][fisher] = None
        sharks[size] = (None, -1, -1)
        break

    new_board = [[None for _ in range(c)] for _ in range(r)]
    for size, (pos, s, d) in sharks.items():
        if pos is None:
            continue
        x, y = pos

        next_x, next_y, d = move(c, r, x, y, s, d)
        if new_board[next_y][next_x] is None or new_board[next_y][next_x] < size:
            if new_board[next_y][next_x] is not None:
                sharks[new_board[next_y][next_x]] = (None, -1, -1)
            new_board[next_y][next_x] = size
            sharks[size] = ((next_x, next_y), s, d)
        else:
            sharks[size] = (None, -1, -1)
    board = new_board


print(answer)
