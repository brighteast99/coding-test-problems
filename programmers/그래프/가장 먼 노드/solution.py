def solution(n, vertex):
    graph = [set() for _ in range(n)]

    for [a, b] in vertex:
        graph[a - 1].add(b - 1)
        graph[b - 1].add(a - 1)

    visited = {0}
    distances = [0 for _ in range(n)]
    queue = [0]
    while len(queue) > 0:
        current = queue.pop(0)

        for node in graph[current]:
            if node in visited:
                continue
            distances[node] = distances[current] + 1
            queue.append(node)
            visited.add(node)

    max_distance = max(distances)
    return len(list(filter(lambda distance: distance == max_distance, distances)))
