def solution(h1, m1, s1, h2, m2, s2):
    t1 = h1 * 3600 + m1 * 60 + s1
    t2 = h2 * 3600 + m2 * 60 + s2

    answer = 0
    if (h1 == 0 or h1 == 12) and m1 == 0 and s1 == 0:
        answer += 1

    def calc_angles(second):
        return (second / 120 % 360, second / 10 % 360, second * 6 % 360)

    angle_h, angle_m, angle_s = calc_angles(t1)
    while t1 < t2:
        next_angle_h, next_angle_m, next_angle_s = calc_angles(t1 + 1)
        next_angle_h, next_angle_m, next_angle_s = next_angle_h or 360, next_angle_m or 360, next_angle_s or 360

        if next_angle_h == next_angle_s or next_angle_m == next_angle_s:
            answer += 1
        else:
            if angle_s < angle_h and next_angle_s >= next_angle_h:
                answer += 1
            if angle_s < angle_m and next_angle_s >= next_angle_m:
                answer += 1

        t1 += 1
        angle_h, angle_m, angle_s = next_angle_h % 360, next_angle_m % 360, next_angle_s % 360

    return answer
