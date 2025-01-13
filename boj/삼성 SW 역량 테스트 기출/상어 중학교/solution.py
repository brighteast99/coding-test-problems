import sys
from collections import deque

ADJACENT_VECTORS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def print_board(board):
    for row in board:
        for cell in row:
            print(f"{cell:2} " if cell is not None else " - ", end=" ")
        print()
    print()


def find_largest_group(n, board):
    visited = set()
    largest_group = set()
    max_rainbow = 0
    for y in range(n):
        for x in range(n):
            if board[y][x] is None or board[y][x] < 1:
                continue

            block = board[y][x]
            queue = deque([(x, y)])
            group = set()
            rainbows = set()
            while len(queue) > 0:
                cur_x, cur_y = queue.popleft()

                if (cur_x, cur_y) in visited:
                    continue
                visited.add((cur_x, cur_y))
                group.add((cur_x, cur_y))
                if board[cur_y][cur_x] == 0:
                    rainbows.add((cur_x, cur_y))

                for dx, dy in ADJACENT_VECTORS:
                    new_x, new_y = cur_x + dx, cur_y + dy
                    if not (0 <= new_x < n and 0 <= new_y < n):
                        continue

                    if board[new_y][new_x] is None:
                        continue

                    if board[new_y][new_x] == block or board[new_y][new_x] == 0:
                        queue.append((new_x, new_y))

            if (len(group) > len(largest_group)) or (
                len(group) == len(largest_group) and len(rainbows) >= max_rainbow
            ):
                largest_group = group
                max_rainbow = len(rainbows)
            visited.difference_update(rainbows)

    return largest_group


def fall(n, board):
    for x in range(n):
        for y in reversed(range(n - 1)):
            if board[y][x] is None or board[y][x] == -1:
                continue

            cur_y = y
            while cur_y + 1 < n and board[cur_y + 1][x] is None:
                board[cur_y + 1][x] = board[cur_y][x]
                board[cur_y][x] = None
                cur_y += 1


def rotate(n, board):
    return [[board[x][n - 1 - y] for x in range(n)] for y in range(n)]


n, m = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

score = 0
while True:
    largest_group = find_largest_group(n, board)

    # print("board")
    # print_board(board)

    if len(largest_group) < 2:
        break

    for x, y in largest_group:
        board[y][x] = None
    score += len(largest_group) ** 2

    # print("score:", score)
    # print_board(board)

    # print("fall")
    fall(n, board)
    # print_board(board)

    # print("rotate")
    board = rotate(n, board)
    # print_board(board)

    # print("fall")
    fall(n, board)
    # print_board(board)
print(score)
