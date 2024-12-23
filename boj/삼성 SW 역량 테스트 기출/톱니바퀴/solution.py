import sys
from collections import deque

gears = list()
for _ in range(4):
    gears.append(deque(int(num) for num in sys.stdin.readline()[:-1]))


k = int(sys.stdin.readline())
for _ in range(k):
    n, direction = map(int, sys.stdin.readline().split())
    n -= 1
    affected = [i == n for i in range(4)]

    for i in reversed(range(n)):
        affected[i] = gears[i][2] != gears[i + 1][6]
        if not affected[i]:
            break
    for i in range(n + 1, 4):
        affected[i] = gears[i - 1][2] != gears[i][6]
        if not affected[i]:
            break

    for i, gear in enumerate(gears):
        if affected[i]:
            gear.rotate(direction * (-1) ** abs(n - i))


print(sum(2 ** (idx) if gear[0] else 0 for idx, gear in enumerate(gears)))
