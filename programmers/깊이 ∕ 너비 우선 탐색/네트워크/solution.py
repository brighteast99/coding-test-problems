def solution(n, computers):
    answer = 0
    unlinked = {i for i in range(n)}

    while len(unlinked) > 0:
        start = unlinked.pop()
        queue = [start]
        visited = {start}
        while len(queue) > 0:
            cur = queue.pop(0)

            for node, is_linked in enumerate(computers[cur]):
                if is_linked == 0:
                    continue

                if node in visited:
                    continue

                unlinked.remove(node)
                visited.add(node)
                queue.append(node)
        answer += 1

    return answer
