def solution(arrows):
    DELTA = {
        0: (0, 1),
        1: (1, 1),
        2: (1, 0),
        3: (1, -1),
        4: (0, -1),
        5: (-1, -1),
        6: (-1, 0),
        7: (-1, 1),
    }

    answer = 0
    cur = (0, 0)
    nodes, edges = {cur}, set()
    for arrow in arrows:
        dx, dy = DELTA[arrow]
        nxt = (cur[0] + dx, cur[1] + dy)

        if (cur, nxt) not in edges:
            if nxt in nodes:
                answer += 1
            if ((cur[0], nxt[1]), (nxt[0], cur[1])) in edges:
                answer += 1

        nodes.add(nxt)
        edges.update({(cur, nxt), (nxt, cur)})
        cur = nxt

    return answer
