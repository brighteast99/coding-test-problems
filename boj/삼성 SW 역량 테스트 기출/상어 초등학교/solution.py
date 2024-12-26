import sys

n = int(sys.stdin.readline())
seats = [[None] * n for _ in range(n)]
empty_seats = [(x, y) for x in range(n) for y in range(n)]
student_likes = {}


def get_adjacent(n, seats, x, y, likes=None):
    vectors = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    answer = 0
    for dx, dy in vectors:
        if not (0 <= x + dx < n and 0 <= y + dy < n):
            continue

        if likes == None:
            answer += 1 if seats[y + dy][x + dx] is None else 0
        else:
            answer += 1 if seats[y + dy][x + dx] in likes else 0

    return answer


for _ in range(n**2):
    student, *likes = map(int, sys.stdin.readline().split())
    student_likes[student] = likes
    empty_seats.sort(
        key=lambda seat: (
            -get_adjacent(n, seats, seat[0], seat[1], likes),
            -get_adjacent(n, seats, seat[0], seat[1]),
            seat[1],
            seat[0],
        ),
        reverse=True,
    )
    x, y = empty_seats.pop()
    seats[y][x] = student

answer = 0
for y in range(n):
    for x in range(n):
        student = seats[y][x]
        answer += int(10 ** (get_adjacent(n, seats, x, y, student_likes[student]) - 1))

print(answer)
