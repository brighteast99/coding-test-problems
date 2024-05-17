def solution(s):
    answer = 0

    i = 0
    while i < len(s):
        char = s[i]
        count = [1, 0]

        while count[0] != count[1]:
            i += 1

            if i >= len(s):
                return answer + 1

            check = s[i]
            count[0 if char == check else 1] += 1

        answer += 1
        i += 1

    return answer