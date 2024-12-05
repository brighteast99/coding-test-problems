def solution(citations):
    citations.sort(reverse=True)
    h = 0
    for i, citation in enumerate(citations):
        h = max(h, min(i + 1, citation))
    return h
