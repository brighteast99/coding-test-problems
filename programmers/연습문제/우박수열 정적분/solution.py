def solution(k, ranges):
    term = k
    integrals = []
    while term > 1:
        prev_term = term
        term = term // 2 if term % 2 == 0 else term * 3 + 1
        integrals.append(min(prev_term, term) + abs(prev_term - term) / 2)

    answer = []
    for [start, end] in ranges:
        if len(integrals) + end < start:
            answer.append(-1)
            continue
        answer.append(sum(integrals[start:len(integrals) + end]))

    return answer
