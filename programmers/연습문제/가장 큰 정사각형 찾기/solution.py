def solution(board):
    dp = [row[:] for row in board]
    max_size = 0
    for y in range(len(dp)):
        for x in range(len(dp[y])):
            if dp[y][x] == 0:
                continue

            if y > 0 and x > 0 :
                dp[y][x] = min(dp[y-1][x-1], dp[y-1][x], dp[y][x-1]) + 1

            max_size = max(max_size, dp[y][x]**2)
    return max_size
