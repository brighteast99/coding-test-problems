import sys

n, m = map(int, sys.stdin.readline().split())
board = []

for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))

tetrominos = [
    # I shapes
    set([(0, 0), (1, 0), (2, 0), (3, 0)]),
    set([(0, 0), (0, 1), (0, 2), (0, 3)]),
    # square
    set([(0, 0), (1, 0), (0, 1), (1, 1)]),
    # L shapes
    set([(0, 0), (0, 1), (0, 2), (1, 2)]),
    set([(1, 0), (1, 1), (1, 2), (0, 2)]),
    set([(0, 1), (1, 1), (2, 1), (2, 0)]),
    set([(0, 0), (1, 0), (2, 0), (2, 1)]),
    set([(0, 0), (1, 0), (1, 1), (1, 2)]),
    set([(0, 0), (1, 0), (0, 1), (0, 2)]),
    set([(0, 0), (1, 0), (2, 0), (0, 1)]),
    set([(0, 0), (0, 1), (1, 1), (2, 1)]),
    # Z shapes
    set([(0, 0), (0, 1), (1, 1), (1, 2)]),
    set([(0, 1), (1, 0), (1, 1), (2, 0)]),
    set([(1, 0), (1, 1), (0, 1), (0, 2)]),
    set([(0, 0), (1, 0), (1, 1), (2, 1)]),
    # T shapes
    set([(0, 0), (1, 0), (1, 1), (2, 0)]),
    set([(0, 1), (1, 0), (1, 1), (1, 2)]),
    set([(0, 1), (1, 0), (1, 1), (2, 1)]),
    set([(0, 0), (0, 1), (1, 1), (0, 2)]),
]

answer = 0

for y in range(n):
    for x in range(m):
        for tetromino in tetrominos:
            sum = 0
            for dx, dy in tetromino:
                if not (0 <= x + dx < m and 0 <= y + dy < n):
                    break
                sum += board[y + dy][x + dx]
            else:
                answer = max(answer, sum)

print(answer)
