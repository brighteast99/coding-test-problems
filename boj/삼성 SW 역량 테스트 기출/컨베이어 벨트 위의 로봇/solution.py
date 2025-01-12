import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
a = deque(map(int, sys.stdin.readline().split()))
broken = 0
robots = deque()

steps = 0
while broken < k:
    a.rotate()
    for i in range(len(robots)):
        robots[i] += 1
    if len(robots) > 0 and robots[-1] == n - 1:
        robots.pop()

    for i in reversed(range(len(robots))):
        if i < len(robots) - 1 and robots[i + 1] == robots[i] + 1:
            continue
        if a[robots[i] + 1] > 0:
            robots[i] += 1
            a[robots[i]] -= 1
            if a[robots[i]] == 0:
                broken += 1
            if robots[i] == n - 1:
                robots.pop()
                len(robots) -= 1

    if a[0] > 0:
        robots.appendleft(0)
        a[0] -= 1
        if a[0] == 0:
            broken += 1

    steps += 1

print(steps)
