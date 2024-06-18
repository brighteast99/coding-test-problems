def solution(n, info):
    answer = [-1]
    max_gap = 0
    stack = [([0] * 11, 10, n, 0)]
    while stack:
        info_ryan, score, arrows_left, gap = stack.pop()

        if score == 0:
            info_ryan[10] = arrows_left
            if gap < max_gap or gap <= 0:
                continue
            if gap == max_gap and ''.join(map(str, reversed(answer))) > ''.join(map(str, reversed(info_ryan))):
                continue
            answer = info_ryan
            max_gap = gap
            continue

        stack.append((info_ryan[:], score - 1, arrows_left, gap -
                      score if info[10 - score] else gap))
        if arrows_left > info[10 - score]:
            stack.append((info_ryan[:10 - score] + [info[10 - score] + 1] + info_ryan[10 - score + 1:], score - 1, arrows_left -
                         (info[10 - score] + 1), gap + score))

    return answer
