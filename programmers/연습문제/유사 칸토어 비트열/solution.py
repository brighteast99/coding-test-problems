def solution(n, l, r):
    if n == 0:
        return 1

    if l == 1 and r == 5 ** n:
        return 4 ** n

    part_size = 5 ** (n - 1)
    zero_start, zero_end = 2 * part_size + 1, 3 * part_size

    if zero_start <= l <= r <= zero_end:
        return 0

    if r <= zero_end:
        r = min(r, zero_start - 1)
        if r <= part_size:
            return solution(n - 1, l, r)
        if l <= part_size < r:
            return solution(n - 1, l, part_size) + solution(n - 1, 1, r - part_size)
        return solution(n - 1, l - part_size, r - part_size)

    if zero_start <= l:
        l = max(l, zero_end + 1)
        return solution(n, 5 ** n + 1 - r, 5 ** n + 1 - l)

    return solution(n, l, zero_start - 1) + solution(n, zero_end + 1, r)
