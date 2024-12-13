def solution(numbers, target):
    stack = [(-1, 0)]
    answer = 0
    while len(stack):
        (idx, accum) = stack.pop()
        idx += 1
        if idx == len(numbers):
            if accum == target:
                answer += 1
            continue

        stack.extend([(idx, accum + numbers[idx]), (idx, accum - numbers[idx])])

    return answer
