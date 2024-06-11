def solution(storey):
    answer = 0
    while storey > 0:
        digit = storey % 10
        if digit >= 5:
            if digit > 5 or storey // 10 % 10 >= 5:
                storey += 10
            digit = 10 - digit
        answer += digit
        storey //= 10
    return answer
