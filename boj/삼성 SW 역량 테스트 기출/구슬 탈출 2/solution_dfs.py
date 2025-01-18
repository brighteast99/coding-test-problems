import sys

EMPTY, WALL, HOLE, RED, BLUE = ".", "#", "O", "R", "B"
UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3
VECTORS = [(0, -1), (0, 1), (-1, 0), (1, 0)]
visited_states = {}


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


def dfs(board, hole, red, blue, moves=0, direction=None):
    visited_states[(red, blue)] = moves

    if moves == 10:
        return -1

    if direction is not None:
        moves += 1
        if (
            (red[0] == blue[0] and blue[1] < red[1] and direction == UP)
            or (red[0] == blue[0] and blue[1] > red[1] and direction == DOWN)
            or (red[1] == blue[1] and blue[0] < red[0] and direction == LEFT)
            or (red[1] == blue[1] and blue[0] > red[0] and direction == RIGHT)
        ):
            blue = move_marble(board, blue, direction)
            red = move_marble(board, red, direction, blue)
        else:
            red = move_marble(board, red, direction)
            blue = move_marble(board, blue, direction, red if red != hole else None)

        if blue == hole:
            return -1

        if red == hole:
            return moves

        if (red, blue) in visited_states and visited_states[(red, blue)] < moves:
            return -1

    min_moves = -1
    for direction in range(4):
        cur_moves = dfs(board, hole, red, blue, moves, direction)
        if cur_moves == -1:
            continue
        if min_moves == -1:
            min_moves = cur_moves
        else:
            min_moves = min(min_moves, cur_moves)

    return min_moves


n, m = map(int, sys.stdin.readline().split())
board = [[cell for cell in sys.stdin.readline()[:-1]] for _ in range(n)]
positions = {HOLE: None, RED: None, BLUE: None}

for y in range(n):
    for x in range(m):
        if board[y][x] == HOLE or board[y][x] == RED or board[y][x] == BLUE:
            positions[board[y][x]] = (x, y)
            if board[y][x] != HOLE:
                board[y][x] = EMPTY


answer = dfs(board, positions[HOLE], positions[RED], positions[BLUE])
print(answer)
