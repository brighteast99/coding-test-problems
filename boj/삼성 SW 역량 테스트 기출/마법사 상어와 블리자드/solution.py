import sys


def conv_direction(direction):
    if direction == 1:
        return 4
    if direction == 2:
        return 2
    if direction == 3:
        return 1
    else:
        return 3


def pad_or_trim_orbs(orbs, n):
    if len(orbs) < n:
        orbs.extend([0] * (n - len(orbs)))
    else:
        while len(orbs) > n:
            orbs.pop()


def blizard(orbs, direction, distance):
    idx = 0
    gap = direction * 2 - 1
    for _ in range(distance):
        idx += gap
        if idx >= len(orbs):
            break
        gap += 8
        orbs[idx] = 0


def remove_gaps(orbs):
    new_orbs = [0]
    for orb in orbs[1:]:
        if orb > 0:
            new_orbs.append(orb)

    pad_or_trim_orbs(new_orbs, len(orbs))
    return new_orbs


def explode(orbs):
    score = 0

    i = 1
    while i < len(orbs):
        if orbs[i] == 0:
            i += 1
            continue

        end = i + 1
        while end < len(orbs) and orbs[end] == orbs[i]:
            end += 1

        chunk_size = end - i
        if chunk_size >= 4:
            score += orbs[i] * chunk_size
            for group_idx in range(i, end):
                orbs[group_idx] = 0

        i = end

    return score


def conv_orbs(orbs):
    new_orbs = [0]

    i = 1
    while i < len(orbs):
        if orbs[i] == 0:
            i += 1
            continue

        end = i + 1
        while end < len(orbs) and orbs[end] == orbs[i]:
            end += 1

        new_orbs.extend([end - i, orbs[i]])
        i = end

    pad_or_trim_orbs(new_orbs, len(orbs))
    return new_orbs


n, m = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
orbs = [0]
N_ORBS = n**2

DIRECTIONS = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}
moves = zip(
    sum([[i] * 2 for i in range(1, n)], []) + [n - 1], [i % 4 for i in range(2 * n - 1)]
)
x, y = (n // 2, n // 2)
while True:
    for dist, direction in moves:
        dx, dy = DIRECTIONS[direction]
        for _ in range(dist):
            x, y = (x + dx, y + dy)
            orbs.append(board[y][x])
    if (x, y) == (0, 0):
        break


score = 0
for _ in range(m):
    d, s = map(int, sys.stdin.readline().split())

    d = conv_direction(d)

    blizard(orbs, d, s)
    orbs = remove_gaps(orbs)
    while True:
        cur_score = explode(orbs)
        if cur_score == 0:
            break
        orbs = remove_gaps(orbs)
        score += cur_score
    orbs = conv_orbs(orbs)

print(score)
