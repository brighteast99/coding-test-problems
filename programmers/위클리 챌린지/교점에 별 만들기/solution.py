from itertools import combinations


def solution(line):
    INF = float('inf')

    pairs = combinations(line, 2)
    intersections = set()
    min_x, max_x = INF, -INF
    min_y, max_y = INF, -INF
    for ([A, B, E], [C, D, F]) in pairs:
        denominator = A * D - B * C
        if denominator == 0:
            continue

        x, y = (B * F - E * D) / denominator, (E * C - A * F) / denominator
        if not x.is_integer() or not y.is_integer():
            continue

        x, y = int(x), int(y)
        intersections.add((x, y))
        min_x, max_x = min(min_x, x), max(max_x, x)
        min_y, max_y = min(min_y, y), max(max_y, y)

    return [''.join(['*' if (x, y) in intersections else '.'
                     for x in range(min_x, max_x + 1)])
            for y in reversed(range(min_y, max_y + 1))]
