import sys

sys.setrecursionlimit(10**6)


def solution(money):
    answer = 0
    dp = dict()

    def find_max(start, end):
        label = f"{start}-{end}"

        if end < start:
            return 0

        if label in dp:
            return dp[label]

        if start == end:
            dp[label] = money[start]
        else:
            dp[label] = max(
                money[start] + find_max(start + 2, end), find_max(start + 1, end)
            )

        return dp[label]

    return max(money[0] + find_max(2, len(money) - 2), find_max(1, len(money) - 1))
