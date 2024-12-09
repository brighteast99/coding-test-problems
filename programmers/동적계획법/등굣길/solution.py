def solution(m, n, puddles):
    map = [[0 for _ in range(m)] for _ in range(n)]
    map[0][0] = 1

    for y in range(n):
        for x in range(m):
            if any(puddle[0] - 1 == x and puddle[1] - 1 == y for puddle in puddles):
                print("continue:", x, y)
                continue

            if x > 0:
                map[y][x] += map[y][x - 1]
                map[y][x] %= 1_000_000_007
            if y > 0:
                map[y][x] += map[y - 1][x]
                map[y][x] %= 1_000_000_007

    return map[n - 1][m - 1]
