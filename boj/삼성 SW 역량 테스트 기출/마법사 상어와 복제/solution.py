import itertools
import sys
from collections import deque

DIRECTIONS = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]


def select_path(board, x, y):
    possible_moves = []

    max_score = 0
    for moves in itertools.product([0, 2, 4, 6], repeat=3):
        cur_x, cur_y = x, y
        score = 0
        visited = set((x, y))
        for direction in moves:
            dx, dy = DIRECTIONS[direction]
            next_x, next_y = cur_x + dx, cur_y + dy
            if not (0 <= next_x < 4 and 0 <= next_y < 4):
                break
            if (next_x, next_y) in visited:
                continue
            cur_x, cur_y = next_x, next_y
            visited.add((cur_x, cur_y))
            score += len(board[cur_y][cur_x])
        else:
            if score > max_score:
                max_score = score
                possible_moves = []
            if score >= max_score:
                possible_moves.append(moves)
        continue

    ORDER = {2: 0, 0: 1, 6: 2, 4: 3}
    possible_moves.sort(
        key=lambda moves: (ORDER[moves[0]], ORDER[moves[1]], ORDER[moves[2]])
    )

    return possible_moves[0]


m, s = map(int, sys.stdin.readline().split())
board = [[list() for _ in range(4)] for _ in range(4)]

for _ in range(m):
    y, x, d = map(int, sys.stdin.readline().split())

    board[y - 1][x - 1].append(d - 1)

shark_y, shark_x = map(int, sys.stdin.readline().split())
shark_x, shark_y = shark_x - 1, shark_y - 1

smells = deque([[], []])
for _ in range(s):
    new_board = [[list() for _ in range(4)] for _ in range(4)]
    for y in range(4):
        for x in range(4):
            for direction in board[y][x]:
                for _ in range(8):
                    dx, dy = DIRECTIONS[direction]
                    next_x, next_y = x + dx, y + dy
                    if not (0 <= next_x < 4 and 0 <= next_y < 4):
                        direction = (direction - 1) % 8
                        continue
                    if (next_x, next_y) == (shark_x, shark_y) or any(
                        (next_x, next_y) in smell for smell in smells
                    ):
                        direction = (direction - 1) % 8
                        continue
                    new_board[next_y][next_x].append(direction)
                    break
                else:
                    new_board[y][x].append(direction)
                    continue

    moves = select_path(new_board, shark_x, shark_y)
    smell = []
    for direction in moves:
        dx, dy = DIRECTIONS[direction]
        shark_x, shark_y = shark_x + dx, shark_y + dy
        if len(new_board[shark_y][shark_x]) > 0:
            smell.append((shark_x, shark_y))
        new_board[shark_y][shark_x] = list()
    smells.popleft()
    smells.append(smell)

    for y in range(4):
        for x in range(4):
            board[y][x].extend(new_board[y][x])

print(sum(sum(map(lambda cell: len(cell), row)) for row in board))
