import sys

DIRECTIONS = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]


def dfs(board, fishes, x, y, score=0):
    if board[y][x][0] == 0:
        return score

    board = [[board[_y][_x] for _x in range(4)] for _y in range(4)]
    direction = board[y][x][1]
    score += board[y][x][0]
    fishes = {**fishes}
    fishes[board[y][x][0]] = None
    board[y][x] = 0, -1

    dx, dy = DIRECTIONS[direction]

    if not (0 <= x + dx < 4 and 0 <= y + dy < 4):
        return score

    for fish in range(1, 17):
        pos = fishes[fish]
        if pos is None:
            continue
        fish_x, fish_y = pos
        fish_direction = board[fish_y][fish_x][1]

        for i in range(8):
            cur_direction = (fish_direction + i) % 8
            fish_dx, fish_dy = DIRECTIONS[cur_direction]
            new_x, new_y = fish_x + fish_dx, fish_y + fish_dy

            if not (0 <= new_x < 4 and 0 <= new_y < 4):
                continue
            if x == new_x and y == new_y:
                continue

            fishes[fish] = (new_x, new_y)
            fishes[board[new_y][new_x][0]] = (fish_x, fish_y)
            board[fish_y][fish_x] = board[new_y][new_x]
            board[new_y][new_x] = (fish, cur_direction)
            break

    max_score = score
    dist = 1
    while 0 <= x + dx * dist < 4 and 0 <= y + dy * dist < 4:
        max_score = max(
            max_score, dfs(board, fishes, x + dx * dist, y + dy * dist, score)
        )
        dist += 1

    return max_score


board = [[(0, -1)] * 4 for _ in range(4)]
fishes = {key: None for key in range(17)}

for y in range(4):
    line = list(map(int, sys.stdin.readline().split()))
    for x in range(4):
        board[y][x] = (line[x * 2], line[x * 2 + 1] - 1)
        fishes[line[x * 2]] = (x, y)


print(dfs(board, fishes, 0, 0))
