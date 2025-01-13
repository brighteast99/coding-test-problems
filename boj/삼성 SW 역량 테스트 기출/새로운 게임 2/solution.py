import sys

DIRECTION_VECTORS = [(1, 0), (0, -1), (-1, 0), (0, 1)]
WHITE, RED, BLUE = 0, 1, 2

n, k = map(int, sys.stdin.readline().split())
board = [
    list(map(lambda color: [int(color), []], sys.stdin.readline().split()))
    for _ in range(n)
]

pieces = {num: None for num in range(k)}

for num in range(k):
    y, x, direction = map(int, sys.stdin.readline().split())
    if direction == 1 or direction == 4:
        direction -= 1
    elif direction == 3:
        direction = 1
    pieces[num] = [(x - 1, y - 1), direction]
    board[y - 1][x - 1][1].append(num)


time = 0
while time < 1000:
    time += 1
    for num in range(k):
        (x, y), direction = pieces[num]

        piece_idx = board[y][x][1].index(num)
        stack = board[y][x][1][piece_idx:]
        board[y][x][1] = board[y][x][1][:piece_idx]

        dx, dy = DIRECTION_VECTORS[direction]
        if (
            not (0 <= x + dx < n and 0 <= y + dy < n)
            or board[y + dy][x + dx][0] == BLUE
        ):
            direction = (direction + 2) % 4
            dx, dy = DIRECTION_VECTORS[direction]
            if (
                not (0 <= x + dx < n and 0 <= y + dy < n)
                or board[y + dy][x + dx][0] == BLUE
            ):
                dx, dy = 0, 0
        if board[y + dy][x + dx][0] == RED:
            if dx != 0 or dy != 0:
                stack = stack[::-1]

        for piece in stack:
            pieces[piece][0] = (x + dx, y + dy)
            if num == piece:
                pieces[piece][1] = direction

        board[y + dy][x + dx][1].extend(stack)
        if len(board[y + dy][x + dx][1]) >= 4:
            break
    else:
        continue
    break
else:
    time = -1

print(time)
