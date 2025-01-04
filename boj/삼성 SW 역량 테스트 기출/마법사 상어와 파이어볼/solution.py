import sys

n, m, k = map(int, sys.stdin.readline().split())

fireballs = []

for _ in range(m):
    r, c, m, s, d = map(int, sys.stdin.readline().split())
    fireballs.append(((r, c), m, s, d))

vectors = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]
for _ in range(k):
    new_fireballs = {}
    for i, ((r, c), m, s, d) in enumerate(fireballs):
        dx, dy = vectors[d]
        new_r, new_c = (r + dy * s) % n, (c + dx * s) % n
        if (new_r, new_c) in new_fireballs:
            new_fireballs[(new_r, new_c)].append((m, s, d))
        else:
            new_fireballs[(new_r, new_c)] = [(m, s, d)]

    fireballs = []
    for r, c in new_fireballs.keys():
        n_fireballs = len(new_fireballs[(r, c)])
        if n_fireballs > 1:
            m, s, sum_d = 0, 0, 0

            for fireball in new_fireballs[(r, c)]:
                m += fireball[0]
                s += fireball[1]
                sum_d += fireball[2] % 2

            m //= 5
            if m == 0:
                continue

            s //= n_fireballs
            if sum_d == n_fireballs or sum_d == 0:
                directions = [0, 2, 4, 6]
            else:
                directions = [1, 3, 5, 7]

            for d in directions:
                fireballs.append(((r, c), m, s, d))

        else:
            m, s, d = new_fireballs[(r, c)][0]
            fireballs.append(((r, c), m, s, d))


print(sum(map(lambda fireball: fireball[1], fireballs)))
