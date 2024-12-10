def solution(N, number):
    if N == number:
        return 1

    table = [set() for _ in range(9)]
    table[1].add(N)
    for n_count in range(2, 9):
        table[n_count].add(int(str(N) * n_count))
        for i in range(1, n_count):
            for a in table[i]:
                for b in table[n_count - i]:
                    table[n_count].add(a + b)
                    table[n_count].add(a - b)
                    table[n_count].add(a * b)
                    if b != 0:
                        table[n_count].add(a // b)
        if number in table[n_count]:
            return n_count

    return -1
