def solution(N, road, K):
    graph = [[float('inf') if start != end else 0 for end in range(N)] for start in range(N)]
    graph[0][0] = 0

    for [start, end, dist] in road:
        min_dist = min(graph[start-1][end-1], dist)
        graph[start-1][end-1] = min_dist
        graph[end-1][start-1] = min_dist

    dp = graph[0][:]
    visited = [False for _ in range(N)]
    while True:
        node = None
        for i in range(N):
            if visited[i]:
                continue
            if node is None or dp[i] < dp[node]:
                node = i

        if node is None:
            break

        for i in range(N):
            dp[i] = min(dp[i], \
                            dp[node] + graph[node][i])

        visited[node] = True

    return len(list(filter(lambda dist: dist <= K, dp)))
