from functools import reduce

def solution(k, m, score):
    score.sort(reverse=True)

    boxes = [score[i:min(i + m, len(score))] for i in range(0, len(score), m)]
    if len(boxes[-1]) < m:
        boxes.pop()

    return reduce(lambda acc, cur: acc + m * cur[-1], boxes, 0)
