BURGER = [1, 2, 3, 1]

def solution(ingredient):
    answer = 0

    stack = []
    for i in range(len(ingredient)):
        stack.append(ingredient[i])
        if stack[-4:] ==  BURGER:
            answer += 1
            del stack[-4:]

    return answer
