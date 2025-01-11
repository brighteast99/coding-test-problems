import sys
from collections import deque

ADJACENT_DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def firestorm(board_size, board, l):
    cell_size = 2**l
    new_board = [[0] * board_size for _ in range(board_size)]

    for y in range(board_size):
        for x in range(board_size):
            base_x, base_y = (x // cell_size) * cell_size, (y // cell_size) * cell_size
            rel_x, rel_y = x % cell_size, y % cell_size

            new_board[base_y + rel_x][base_x + cell_size - 1 - rel_y] = board[y][x]

    shrink = set()
    for y in range(board_size):
        for x in range(board_size):
            if new_board[y][x] == 0:
                continue
            adjacent_ice = 0
            for dx, dy in ADJACENT_DIRECTIONS:
                if not (0 <= x + dx < board_size and 0 <= y + dy < board_size):
                    continue
                if new_board[y + dy][x + dx] > 0:
                    adjacent_ice += 1

            if adjacent_ice < 3:
                shrink.add((x, y))

    for x, y in shrink:
        new_board[y][x] -= 1

    return new_board


n, q = map(int, sys.stdin.readline().split())
board_size = 2**n
board = [list(map(int, sys.stdin.readline().split())) for _ in range(board_size)]
spells = list(map(int, sys.stdin.readline().split()))

for l in spells:
    board = firestorm(board_size, board, l)

total_ice = 0
max_ice_area = 0
visited = set()
for y in range(board_size):
    for x in range(board_size):
        if (x, y) in visited or board[y][x] == 0:
            continue

        queue = deque([(x, y)])
        ice_area = 0
        while len(queue) > 0:
            cur_x, cur_y = queue.popleft()

            if (cur_x, cur_y) in visited:
                continue
            visited.add((cur_x, cur_y))
            ice_area += 1
            total_ice += board[cur_y][cur_x]

            for dx, dy in ADJACENT_DIRECTIONS:
                if not (0 <= cur_x + dx < board_size and 0 <= cur_y + dy < board_size):
                    continue
                if board[cur_y + dy][cur_x + dx] == 0:
                    continue

                queue.append((cur_x + dx, cur_y + dy))
        max_ice_area = max(max_ice_area, ice_area)

print(total_ice)
print(max_ice_area)
