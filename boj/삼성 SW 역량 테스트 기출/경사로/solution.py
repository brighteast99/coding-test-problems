import sys

n, l = map(int, sys.stdin.readline().split())
board = []

for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))

roads = [*board, *[[row[c] for row in board] for c in range(n)]]


def passable(road, l):
    start_idx, last_height = 0, road[0]
    cur_idx = 0
    while True:
        cur_idx += 1
        if cur_idx == len(road):
            break

        height = road[cur_idx]
        if abs(height - last_height) > 1:
            return False
        if height == last_height:
            continue

        if height > last_height:
            if cur_idx - start_idx >= l:
                start_idx, last_height = cur_idx, height
                continue
            else:
                return False
        else:
            for _ in range(1, l):
                cur_idx += 1
                if cur_idx >= len(road) or road[cur_idx] != height:
                    return False
            start_idx, last_height = cur_idx + 1, height

    return True


answer = 0
for road in roads:
    if passable(road, l):
        answer += 1
print(answer)
