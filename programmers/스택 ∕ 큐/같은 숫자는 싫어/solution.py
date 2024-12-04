def solution(arr):
    answer = []
    for num in arr:
        try:
            if num != answer[-1]:
                answer.append(num)
        except IndexError:
            answer.append(num)
    return answer
