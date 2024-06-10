def solution(w,h):
    if h == 1:
        return 0

    if w == h:
        return w * h - w

    answer = 0
    for x in range(w):
        answer += x * h // w
    return answer * 2
