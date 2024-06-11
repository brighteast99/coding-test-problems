def solution(n):
    answer = 0
    stack = [[] * n]
    while len(stack) > 0:
        queens = stack.pop()

        if len(queens) == n:
            answer += 1
            continue

        for next_queen in range(n):
            if next_queen in queens:
                continue
            for (row, queen) in enumerate(queens):
                if abs(queen - next_queen) == len(queens) - row:
                    break
            else:
                stack.append(queens + [next_queen])
    return answer
