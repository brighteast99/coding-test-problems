import math

def num_divisors(number):
    divisors = 0

    limit = math.floor(math.pow(number, 1/2))

    for i in range(1, limit + 1):
        if number % i == 0:
            divisors += 2
        if i ** 2 == number:
            divisors -= 1
    return divisors


def solution(number, limit, power):
    answer = 0

    for i in range (1, number + 1):
        divisors = num_divisors(i)
        if divisors > limit:
            answer += power
        else:
            answer += divisors
    return answer
