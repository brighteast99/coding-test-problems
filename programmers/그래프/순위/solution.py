def find_reachable(nodes, start, direction):
    reachable_nodes = {*nodes[start][direction]}
    while True:
        size = len(reachable_nodes)
        new_reachable_nodes = set()
        for reachable_node in reachable_nodes:
            new_reachable_nodes.update(nodes[reachable_node][direction])
        reachable_nodes.update(new_reachable_nodes)

        if size == len(reachable_nodes):
            return reachable_nodes


def solution(n, results):
    nodes = {key: {"inbound": set(), "outbound": set()} for key in range(1, n + 1)}
    for winner, loser in results:
        nodes[winner]["outbound"].add(loser)
        nodes[loser]["inbound"].add(winner)

    answer = 0
    for node in nodes:
        inbounds = find_reachable(nodes, node, "inbound")
        outbounds = find_reachable(nodes, node, "outbound")
        if len(inbounds) + len(outbounds) == n - 1:
            answer += 1

    return answer
