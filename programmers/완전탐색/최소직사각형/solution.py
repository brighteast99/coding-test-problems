def solution(sizes):
    answer = [0, 0]

    for size in sizes:
        [w, h] = size

        if w < h:
            [w, h] = [h, w]

        answer[0] = max(answer[0], w)
        answer[1] = max(answer[1], h)

    return answer[0] * answer[1]
