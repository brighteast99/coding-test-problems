def solution(rows, columns, queries):
    answer = []

    matrix = [[x * columns + (y + 1) for y in range(columns)] for x in range(rows)]
    for (x1, y1, x2, y2) in queries:
        dx, dy = x2 - x1, y2 - y1
        steps_x = [0] * dy + [1] * dx + [0] * dy + [-1] * dx
        steps_y = [1] * dy + [0] * dx + [-1] * dy + [0] * dx

        cur_x, cur_y = x1 - 1, y1 - 1
        num = matrix[cur_x][cur_y]
        min_val = num
        for (step_x, step_y) in zip(steps_x, steps_y):
            next_x, next_y = cur_x + step_x, cur_y + step_y
            min_val = min(min_val, matrix[next_x][next_y])
            matrix[next_x][next_y], num = num, matrix[next_x][next_y]
            cur_x, cur_y = next_x, next_y

        answer.append(min_val)

    return answer
