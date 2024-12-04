def solution(prices):
    stack = []
    answer = list(reversed(range(len(prices))))
    for t, price in enumerate(prices):
        if len(stack) == 0 or prices[stack[-1]] < price:
            stack.append(t)
        else:
            while len(stack) > 0 and prices[stack[-1]] > price:
                popped = stack.pop()
                answer[popped] = t - popped
            stack.append(t)
    return answer
