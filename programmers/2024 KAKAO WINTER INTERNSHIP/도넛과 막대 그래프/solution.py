def solution(edges):
    INCOMING, OUTGOING = 0, 1
    DOUGHNUT, STICK, EIGHT = 1, 2, 3

    nodes = {}
    for (frm, to) in edges:
        if frm not in nodes:
            nodes[frm] = ([], [])
        if to not in nodes:
            nodes[to] = ([], [])
        nodes[frm][OUTGOING].append(to)
        nodes[to][INCOMING].append(frm)

    n_graphs = 0
    for node in nodes:
        if not nodes[node][INCOMING] and len(nodes[node][OUTGOING]) >= 2:
            answer[0] = node
            n_graphs = len(nodes[node][OUTGOING])
            break
    del nodes[answer[0]]

    answer = [0, 0, 0, 0]
    for node in nodes:
        if len(nodes[node][OUTGOING]) == 2:
            answer[EIGHT] += 1
        elif not nodes[node][OUTGOING]:
            answer[STICK] += 1
    answer[DOUGHNUT] = n_graphs - answer[STICK] - answer[EIGHT]

    return answer
