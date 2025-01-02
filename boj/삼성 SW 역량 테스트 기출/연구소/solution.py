import sys
import collections
import itertools

n, m = map(int, sys.stdin.readline().split())
board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))

empty_pos = []
for y in range(n):
    for x in range(m):
        if board[y][x] == 0:
            empty_pos.append((x, y))


def spread(board):
    board = [row.copy() for row in board]
    vectors = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    visited = set()

    for y, row in enumerate(board):
        for x, cell in enumerate(row):
            if (x, y) in visited or board[y][x] != 2:
                continue

            queue = collections.deque([(x, y)])
            while len(queue) > 0:
                cur_x, cur_y = queue.popleft()

                if (cur_x, cur_y) in visited:
                    continue

                visited.add((cur_x, cur_y))
                board[cur_y][cur_x] = 2

                for dx, dy in vectors:
                    if not (
                        0 <= cur_x + dx < len(row) and 0 <= cur_y + dy < len(board)
                    ):
                        continue

                    if board[cur_y + dy][cur_x + dx] == 0:
                        queue.append((cur_x + dx, cur_y + dy))

    return board


def clac_safe_area(board):
    return sum(map(lambda row: row.count(0), board))


answer = 0
for p1, p2, p3 in itertools.combinations(empty_pos, 3):
    board[p1[1]][p1[0]] = 1
    board[p2[1]][p2[0]] = 1
    board[p3[1]][p3[0]] = 1

    answer = max(answer, clac_safe_area(spread(board)))

    board[p1[1]][p1[0]] = 0
    board[p2[1]][p2[0]] = 0
    board[p3[1]][p3[0]] = 0

print(answer)
