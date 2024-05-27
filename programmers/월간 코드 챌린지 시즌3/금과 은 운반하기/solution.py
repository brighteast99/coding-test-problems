import math


def solution(a, b, g, s, w, t):
    def can_build(time):
        S, G, total = 0, 0, 0

        for i in range(len(t)):
            W = min(g[i] + s[i], w[i] * math.floor(time / (2 * t[i]) + 0.5))

            S += min(s[i], W)
            G += min(g[i], W)
            total += W

        return a <= G and b <= S and a + b <= total

    left = 1
    right = max(t) * (a + b) * 2
    while left <= right:
        mid = math.floor((left + right) / 2)

        if can_build(mid):
            right = mid - 1
        else:
            left = mid + 1

    return left
