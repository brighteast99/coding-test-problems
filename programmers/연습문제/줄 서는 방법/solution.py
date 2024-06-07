from math import factorial

def solution(n, k):
    people = [i + 1 for i in range(n)]

    k -= 1
    answer = []
    for i in reversed(range(n)):
        cases = factorial(i)
        order = k // cases
        k %= cases
        answer.append(people.pop(order))

    return answer
