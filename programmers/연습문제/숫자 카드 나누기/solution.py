from functools import reduce


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def solution(arrayA, arrayB):
    arrayA = list(set(arrayA))
    arrayB = list(set(arrayB))

    a1 = reduce(lambda acc, cur: gcd(acc, cur) ,arrayA[1:], arrayA[0])
    if any(num % a1 == 0 for num in arrayB):
        a1 = 0

    a2 = reduce(lambda acc, cur: gcd(acc, cur) ,arrayB[1:], arrayB[0])
    if any(num % a2 == 0 for num in arrayA):
        a2 = 0

    return max(a1, a2)
