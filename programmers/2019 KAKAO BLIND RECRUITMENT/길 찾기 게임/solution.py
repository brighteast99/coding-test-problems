import sys
sys.setrecursionlimit(10000)

def solution(nodeinfo):
    answer = [[], []]
    nodeinfo = sorted([(i+1, x, y) for i, (x, y) in enumerate(nodeinfo)], key=lambda node: node[1])

    def traverse(nodeinfo):
        if len(nodeinfo) > 0:
            child = (0, 0, -1)

            for i, (n, x, y) in enumerate(nodeinfo):
                if y > child[2]:
                    child = (i, n, y)

            answer[0].append(child[1])
            traverse(nodeinfo[:child[0]])
            traverse(nodeinfo[child[0] + 1:])
            answer[1].append(child[1])

    traverse(nodeinfo)
    return answer
