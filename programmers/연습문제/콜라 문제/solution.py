def solution(a, b, n):
    answer = 0

    while n >= a:
        gets = int(n / a) * b
        answer += gets
        n = n % a + gets

    return answer
