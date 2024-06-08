from functools import reduce

def solution(data, col, row_begin, row_end):
    sorted_data = sorted(data, key=lambda row: (row[col - 1], -row[0]))

    answer = 0
    for row in range(row_begin, row_end + 1):
        tpl = sorted_data[row - 1]
        S_row = reduce(lambda acc, cur: acc + (cur % row), tpl, 0)
        answer ^= S_row

    return answer
