SHEEP = 0
WOLF = 1


def scan_descendants(info, child_info, n, node_info):
    node_info[n] = [0, 1] if info[n] == SHEEP else [100, 0]

    for child in child_info[n]:
        [dist, sheeps] = scan_descendants(info, child_info, child, node_info)
        node_info[n][0] = min(node_info[n][0], dist + 1)
        node_info[n][1] += sheeps

    return node_info[n]


def solution(info, edges):
    node_info = [[] for _ in range(len(info))]
    child_info = [[] for _ in range(len(info))]

    for [parent, child] in edges:
        child_info[parent].append(child)

    scan_descendants(info, child_info, 0, node_info)

    sheeps, wolves = 0, 0
    heads = [0]
    while True:
        all_stuck = True
        for head in heads:
            stuck = info[head] == WOLF and wolves >= sheeps - 1
            all_stuck = all_stuck and stuck
            if stuck:
                continue
            else:
                if info[head] == SHEEP:
                    sheeps += 1
                else:
                    wolves += 1

                heads.remove(head)
                heads.extend(child_info[head])
                heads.sort(key=lambda head: (-(node_info[head][0] < sheeps - wolves), -node_info[head][1], node_info[head][0]))
                break

        if all_stuck:
            break

    return sheeps
