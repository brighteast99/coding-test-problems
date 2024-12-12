def solution(arr):
    numbers, operators = [], []
    for i, val in enumerate(arr):
        if i % 2 == 0:
            numbers.append(int(val))
        else:
            operators.append(val)

    l = len(arr) // 2 + 1
    max_table = [
        [numbers[s] if s == e else -1_000_000 for e in range(l)] for s in range(l)
    ]
    min_table = [
        [numbers[s] if s == e else 1_000_000 for e in range(l)] for s in range(l)
    ]

    for window in range(1, l):
        for start in range(0, l - window):
            end = start + window
            for k in range(start, end):
                if operators[k] == "+":
                    max_table[start][end] = max(
                        max_table[start][end],
                        max_table[start][k] + max_table[k + 1][end],
                    )
                    min_table[start][end] = min(
                        min_table[start][end],
                        min_table[start][k] + min_table[k + 1][end],
                    )
                else:
                    max_table[start][end] = max(
                        max_table[start][end],
                        max_table[start][k] - min_table[k + 1][end],
                    )
                    min_table[start][end] = min(
                        min_table[start][end],
                        min_table[start][k] - max_table[k + 1][end],
                    )

    return max_table[0][l - 1]
