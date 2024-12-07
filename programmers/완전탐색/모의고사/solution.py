def solution(answers):
    scores = [0, 0, 0]
    PATTERN_A = [1, 2, 3, 4, 5]
    PATTERN_B = [2, 1, 2, 3, 2, 4, 2, 5]
    PATTERN_C = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i, answer in enumerate(answers):
        if PATTERN_A[i % len(PATTERN_A)] == answer:
            scores[0] += 1
        if PATTERN_B[i % len(PATTERN_B)] == answer:
            scores[1] += 1
        if PATTERN_C[i % len(PATTERN_C)] == answer:
            scores[2] += 1

    max_score = max(scores)
    return [i + 1 for i in range(3) if scores[i] == max_score]
