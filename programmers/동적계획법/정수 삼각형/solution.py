def solution(triangle):
    for i in reversed(range(1, len(triangle))):
        for j in range(len(triangle[i - 1])):
            triangle[i - 1][j] += max(triangle[i][j], triangle[i][j + 1])

    return triangle[0][0]
