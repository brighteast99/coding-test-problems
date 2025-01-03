import collections
import sys

n, l, r = map(int, sys.stdin.readline().split())
board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))

vectors = [(1, 0), (0, 1), (-1, 0), (0, -1)]
days = 0
while True:
    visited = set()
    border_opened = False
    next_board = [row.copy() for row in board]

    for y in range(n):
        for x in range(n):
            if (x, y) in visited:
                continue

            union = set()
            union_people = 0
            queue = collections.deque([(x, y)])
            while len(queue) > 0:
                cur_x, cur_y = queue.popleft()

                if (cur_x, cur_y) in union:
                    continue

                union.add((cur_x, cur_y))
                union_people += board[cur_y][cur_x]

                for dx, dy in vectors:
                    if not (0 <= cur_x + dx < n and 0 <= cur_y + dy < n):
                        continue

                    if (
                        l
                        <= abs(board[cur_y][cur_x] - board[cur_y + dy][cur_x + dx])
                        <= r
                    ):
                        queue.append((cur_x + dx, cur_y + dy))

            union_people //= len(union)
            for union_x, union_y in union:
                next_board[union_y][union_x] = union_people
                border_opened = border_opened or len(union) > 1

            visited.update(union)

    if not border_opened:
        break

    board = next_board

    days += 1

print(days)
