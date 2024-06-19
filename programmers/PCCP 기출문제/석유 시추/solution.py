def solution(land):
    n, m = len(land), len(land[0])
    visited = [[False for __ in range(m)] for _ in range(n)]
    oil = [0] * m

    for y in range(n):
        for x in range(m):
            if visited[y][x]:
                continue

            if not land[y][x]:
                visited[y][x] = True
                continue

            stack = [(x, y)]
            (range_start, range_end) = (x, x)
            size = 0
            while stack:
                (check_x, check_y) = stack.pop()
                if not (0 <= check_x < m) or not (0 <= check_y < n) or visited[check_y][check_x]:
                    continue

                visited[check_y][check_x] = True

                if not land[check_y][check_x]:
                    continue

                size += 1
                range_start = min(range_start, check_x)
                range_end = max(range_end, check_x)

                for (dx, dy) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    stack.append((check_x + dx, check_y + dy))

            for range_x in range(range_start, range_end + 1):
                oil[range_x] += size

    return max(oil)
