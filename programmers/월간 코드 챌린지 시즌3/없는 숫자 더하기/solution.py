def solution(numbers):
    answer = sum([i for i in range(10)])
    for number in numbers:
        answer -= number
    return answer
