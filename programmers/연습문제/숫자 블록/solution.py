def solution(begin, end):
    answer = []
    for idx in range(begin, end + 1):
        if idx == 1:
            answer.append(0)
            continue

        max_divisor = 1
        for n in range(2, int(idx**0.5) + 1):
            if idx % n == 0:
                block = idx // n
                if block <= 10_000_000:
                    answer.append(block)
                    break
                max_divisor = n
        else:
            answer.append(max_divisor)

    return answer
