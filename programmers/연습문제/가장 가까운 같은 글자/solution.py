def solution(s):
    last_idx = {}
    answer = []

    for i in range(len(s)):
        char = s[i]
        answer.append(i - last_idx[char] if char in last_idx else -1)
        last_idx[char]= i

    return answer
