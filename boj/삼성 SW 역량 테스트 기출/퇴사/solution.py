import sys


def dfs(n, councels, day=0):
    if day >= n:
        return 0

    t, p = councels[day]

    if day + t - 1 >= n:
        return dfs(n, councels, day + 1)

    return max(p + dfs(n, councels, day + t), dfs(n, councels, day + 1))


n = int(sys.stdin.readline())
councels = []
for line in sys.stdin.readlines():
    t, p = line.split()
    councels.append((int(t), int(p)))

print(dfs(n, councels))
