def solution(absolutes, signs):
    answer = 0

    for (absolute, sign) in zip(absolutes, signs):
        answer += absolute if sign else -absolute

    return answer
