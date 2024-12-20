import itertools
import sys

n = int(sys.stdin.readline())
s = [list(map(int, line.split())) for line in sys.stdin.readlines()]


def calc(team):
    sum = 0
    for i, j in itertools.combinations(team, 2):
        sum += s[i][j] + s[j][i]
    return sum


answer = 1_000_000
u = set(i for i in range(n))
for combination in itertools.combinations(u, n // 2):
    start = set(combination)
    link = u.difference(start)
    answer = min(answer, abs(calc(start) - calc(link)))

print(answer)
