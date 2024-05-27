def solution(n, s, a, b, fares):
    fare = [[0 if node_from == node_to else float('inf') for node_to in range(n)] for node_from in range(n)]

    for [c, d, f] in fares:
        fare[c-1][d-1] = fare[d-1][c-1] = f

    for node_by in range (n):
        for node_from in range(n):
            for node_to in range(n):
                fare[node_from][node_to] = min(fare[node_from][node_to], fare[node_from][node_by] + fare[node_by][node_to])

    return min(fare[s - 1][middle] + fare[middle][a - 1] + fare[middle][b - 1] for middle in range(n))
