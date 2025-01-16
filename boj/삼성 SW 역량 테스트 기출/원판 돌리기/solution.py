import sys
from collections import deque

ADJACENT_VECTORS = [(-1, 0), (1, 0), (0, 1), (0, -1)]


def remove_adjacents(n, m, plates):
    removed = 0
    for i in range(1, n + 1):
        for j in range(m):
            num = plates[i][j]
            if num == 0:
                continue

            same_numbers = set()
            queue = deque([(i, j)])
            while len(queue) > 0:
                cur_i, cur_j = queue.popleft()

                if (cur_i, cur_j) in same_numbers:
                    continue
                same_numbers.add((cur_i, cur_j))

                for di, dj in ADJACENT_VECTORS:
                    if not (1 <= cur_i + di <= n):
                        continue
                    if plates[cur_i + di][(cur_j + dj) % m] != num:
                        continue
                    queue.append((cur_i + di, (cur_j + dj) % m))

            if len(same_numbers) > 1:
                removed += len(same_numbers)
                for cur_i, cur_j in same_numbers:
                    plates[cur_i][cur_j] = 0

    return removed


n, m, t = map(int, sys.stdin.readline().split())
plates = [deque()] + [deque(map(int, sys.stdin.readline().split())) for _ in range(n)]
numbers_left = n * m

for _ in range(t):
    x, d, k = map(int, sys.stdin.readline().split())
    for plate_num in range(x, n + 1, x):
        plates[plate_num].rotate(k if d == 0 else -k)

    removed = remove_adjacents(n, m, plates)
    numbers_left -= removed
    if numbers_left == 0:
        break

    if removed == 0:
        plate_avg = sum(sum(plate) for plate in plates) / numbers_left
        for i in range(1, n + 1):
            for j in range(m):
                if plates[i][j] == 0:
                    continue
                if plates[i][j] < plate_avg:
                    plates[i][j] += 1
                elif plates[i][j] > plate_avg:
                    plates[i][j] -= 1

print(sum(sum(plate) for plate in plates))
