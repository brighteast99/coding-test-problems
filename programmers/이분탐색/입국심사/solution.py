def solution(n, times):
    left, right = 0, max(times) * (n // len(times) + 1)
    while left < right:
        mid = (left + right) // 2
        if n <= sum(map(lambda time: mid // time, times)):
            right = mid
        else:
            left = mid + 1

    return right
