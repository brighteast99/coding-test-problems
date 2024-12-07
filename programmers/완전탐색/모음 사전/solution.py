def solution(word):
    words = ["A", "E", "I", "O", "U"]
    n = [781, 156, 31, 6, 1]

    answer = 0
    for i, w in enumerate(word):
        answer += 1 + n[i] * words.index(w)

    return answer
