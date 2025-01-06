import sys
from typing import List

r, c, k = map(int, sys.stdin.readline().split())
r, c = r - 1, c - 1
matrix = []

for _ in range(3):
    matrix.append(list(map(int, sys.stdin.readline().split())))


def pivot(matrix: List[List[int]]):
    max_col = max([len(row) for row in matrix])
    return [
        [matrix[r][c] if c < len(matrix[r]) else 0 for r in range(len(matrix))]
        for c in range(max_col)
    ]


time = 0
while True:
    if r < len(matrix) and c < len(matrix[r]):
        if matrix[r][c] == k:
            break

    time += 1

    if time == 101:
        time = -1
        break

    need_pivot = max([len(row) for row in matrix]) > len(matrix)
    if need_pivot:
        matrix = pivot(matrix)
    for i, row in enumerate(matrix):
        freqs = {}
        for n in row:
            if n == 0:
                continue
            if n in freqs:
                freqs[n] += 1
            else:
                freqs[n] = 1
        sorted_row = [[num, freq] for num, freq in freqs.items()]
        sorted_row.sort(key=lambda pair: (pair[1], pair[0]))
        matrix[i] = sum(sorted_row, [])

    if need_pivot:
        matrix = pivot(matrix)

print(time)
