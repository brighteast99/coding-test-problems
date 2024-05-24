def solution(X, Y):
    answer = ''
    numbers = [min(X.count(str(i)), Y.count(str(i))) for i in range(10)]
    for i in reversed(range(10)):
        answer += str(i) * numbers[i]

    if answer.startswith('0'):
        answer = '0'

    return answer or "-1"
