def solution(n):
    if n % 2 == 1:
        return 0
    if n == 2:
        return 3
    if n == 4:
        return 11

    num = 4
    f_2, f_4 = 3, 11
    while num < n:
        num += 2
        f_2, f_4 = f_4, f_4 * 4 - f_2

    return f_4 % 1_000_000_007
