import sys


def find_district(x, y, d1, d2, r, c):
    if c < x - d1:
        return 0 if r < y + d1 else 2
    if x + d2 < c:
        return 1 if r <= y + d2 else 3

    if c <= x and (r - y) + (c - x) < 0:
        return 0

    if x < c and (r - y) - (c - x) < 0:
        return 1

    if c < x - d1 + d2 and (r - (y + d1)) - (c - (x - d1)) > 0:
        return 2

    if x - d1 + d2 <= c and (r - (y + d2)) + (c - (x + d2)) > 0:
        return 3

    return 4


n = int(sys.stdin.readline())
a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]


answer = 100 * n**2
for y in range(0, n - 2):
    for x in range(1, n - 1):
        for d1 in range(1, x + 1):
            for d2 in range(1, n - x):
                if y + d1 + d2 >= n:
                    continue
                districts = [0, 0, 0, 0, 0]
                for r in range(n):
                    for c in range(n):
                        districts[find_district(x, y, d1, d2, r, c)] += a[r][c]
                districts.sort()
                answer = min(answer, districts[4] - districts[0])

print(answer)
