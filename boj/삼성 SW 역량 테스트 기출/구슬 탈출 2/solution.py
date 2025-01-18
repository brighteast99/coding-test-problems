import sys
from collections import deque

EMPTY, WALL, HOLE, RED, BLUE = ".", "#", "O", "R", "B"
UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3
VECTORS = [(0, -1), (0, 1), (-1, 0), (1, 0)]


def move_marble(board, marble, direction, another_marble=None):
    dx, dy = VECTORS[direction]
    new_x, new_y = marble

    while (
        board[new_y + dy][new_x + dx] in [EMPTY, HOLE]
        and (new_x + dx, new_y + dy) != another_marble
    ):
        new_x, new_y = new_x + dx, new_y + dy
        if board[new_y][new_x] == HOLE:
            break

    return (new_x, new_y)


n, m = map(int, sys.stdin.readline().split())
board = [[cell for cell in sys.stdin.readline()[:-1]] for _ in range(n)]
positions = {HOLE: None, RED: None, BLUE: None}

for y in range(n):
    for x in range(m):
        if board[y][x] == HOLE or board[y][x] == RED or board[y][x] == BLUE:
            positions[board[y][x]] = (x, y)
            if board[y][x] != HOLE:
                board[y][x] = EMPTY


answer = -1
queue = deque([(positions[RED], positions[BLUE], 0)])
visited_states = set()
while len(queue) > 0:
    cur_red, cur_blue, moves = queue.popleft()

    if (cur_red, cur_blue) in visited_states:
        continue
    visited_states.add((cur_red, cur_blue))

    if moves == 10:
        break

    for direction in range(4):
        if (
            (cur_red[0] == cur_blue[0] and cur_blue[1] < cur_red[1] and direction == UP)
            or (
                cur_red[0] == cur_blue[0]
                and cur_blue[1] > cur_red[1]
                and direction == DOWN
            )
            or (
                cur_red[1] == cur_blue[1]
                and cur_blue[0] < cur_red[0]
                and direction == LEFT
            )
            or (
                cur_red[1] == cur_blue[1]
                and cur_blue[0] > cur_red[0]
                and direction == RIGHT
            )
        ):
            next_blue = move_marble(board, cur_blue, direction)
            next_red = move_marble(board, cur_red, direction, next_blue)
        else:
            next_red = move_marble(board, cur_red, direction)
            next_blue = move_marble(
                board,
                cur_blue,
                direction,
                next_red if next_red != positions[HOLE] else None,
            )

        if next_blue == positions[HOLE]:
            continue

        if next_red == positions[HOLE]:
            answer = moves + 1
            break

        queue.append((next_red, next_blue, moves + 1))
    else:
        continue

    break
print(answer)
