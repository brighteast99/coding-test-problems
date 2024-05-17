def solution(k, score):
    answer = []

    list = []

    for scr in score:
        if scr > (list[0] if len(list) >= k else -1):
            list.append(scr)
            list.sort()

            if len(list) > k:
                list.pop(0)

        answer.append(list[0])

    return answer