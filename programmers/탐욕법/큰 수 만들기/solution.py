def solution(number, k):
    number = [int(n) for n in number]
    stack = [number.pop(0)]
    for n in number:
        while k > 0 and len(stack):
            if stack[-1] >= n:
                break
            stack.pop()
            k -= 1
        stack.append(n)

    if k > 0:
        stack = stack[:-k]

    return "".join(map(str, stack))
