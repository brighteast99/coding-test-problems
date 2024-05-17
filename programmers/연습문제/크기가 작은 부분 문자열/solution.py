def solution(t, p):
    answer = 0
    length = len(p)
    int_p = int(p)
    for i in range(len(t)-length+1):
        partial = int(t[i:i+length])
        if partial <= int_p:
            answer += 1
    return answer