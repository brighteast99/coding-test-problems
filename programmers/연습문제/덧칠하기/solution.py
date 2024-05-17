def solution(n, m, section):
    answer = 0

    while len(section) > 0:
        cur_section = section.pop(0)
        answer += 1
        while len(section) > 0 and section[0] < cur_section + m:
            section.pop(0)

    return answer