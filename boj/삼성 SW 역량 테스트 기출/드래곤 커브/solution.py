import sys


def rotate(orig, point, direction):
    COS = [1, 0, -1, 0]
    SIN = [0, 1, 0, -1]

    dx, dy = point[0] - orig[0], -(point[1] - orig[1])

    dx, dy = (
        dx * COS[direction] - dy * SIN[direction],
        -(dx * SIN[direction] + dy * COS[direction]),
    )

    return dx + orig[0], dy + orig[1]


curves = {
    0: {
        0: [(0, 0), (1, 0)],
    }
}

for gen in range(0, 11):
    if gen > 0:
        curves[gen] = {}
        prev_curve = curves[gen - 1][0]
        curves[gen][0] = [
            *prev_curve,
            *list(
                map(
                    lambda point: rotate(prev_curve[-1], point, 3),
                    prev_curve[-2::-1],
                )
            ),
        ]
    for direction in [1, 2, 3]:
        curves[gen][direction] = list(
            map(lambda point: rotate((0, 0), point, direction), curves[gen][0])
        )


n = int(sys.stdin.readline())
points_in_curves = set()

for _ in range(n):
    x, y, d, g = map(int, sys.stdin.readline().split())

    curve = [
        (x + dx, y + dy)
        for dx, dy in curves[g][d]
        if 0 <= x + dx <= 100 and 0 <= y + dy <= 100
    ]
    points_in_curves.update(curve)


answer = 0
for x in range(100):
    for y in range(100):
        if all(
            point in points_in_curves
            for point in [(x, y), (x + 1, y), (x, y + 1), (x + 1, y + 1)]
        ):
            answer += 1
print(answer)
