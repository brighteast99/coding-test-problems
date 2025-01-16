import sys
from collections import deque

SPACE, WALL = 0, 1
ADJACENT_VECTORS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def find_passenger(board, passengers, x, y):
    BOARD_SIZE = len(board)

    if len(passengers) == 0:
        return None, -1

    queue = deque([((x, y), 0)])
    visited = set()

    nearest_passengers = []
    min_dist = 2 * BOARD_SIZE
    while len(queue) > 0:
        (cur_x, cur_y), dist = queue.popleft()

        if (cur_x, cur_y) in visited or dist > min_dist:
            continue
        visited.add((cur_x, cur_y))

        if (cur_x, cur_y) in passengers:
            nearest_passengers.append((cur_x, cur_y))
            min_dist = dist

        for dx, dy in ADJACENT_VECTORS:
            if not (0 <= cur_x + dx < BOARD_SIZE and 0 <= cur_y + dy < BOARD_SIZE):
                continue
            if board[cur_y + dy][cur_x + dx] == WALL:
                continue

            queue.append(((cur_x + dx, cur_y + dy), dist + 1))

    if len(nearest_passengers) == 0:
        return None, -1

    nearest_passengers.sort(key=lambda pos: (pos[1], pos[0]))
    return nearest_passengers[0], min_dist


def calc_destination_dist(board, x, y, dest_x, dest_y):
    BOARD_SIZE = len(board)
    queue = deque([((x, y), 0)])
    visited = set()

    while len(queue) > 0:
        (cur_x, cur_y), dist = queue.popleft()

        if (cur_x, cur_y) in visited:
            continue
        visited.add((cur_x, cur_y))

        if (cur_x, cur_y) == (dest_x, dest_y):
            return dist

        for dx, dy in ADJACENT_VECTORS:
            if not (0 <= cur_x + dx < BOARD_SIZE and 0 <= cur_y + dy < BOARD_SIZE):
                continue
            if board[cur_y + dy][cur_x + dx] == WALL:
                continue

            queue.append(((cur_x + dx, cur_y + dy), dist + 1))

    return -1


n, m, fuel = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
passengers = set()
destinations = {}

y, x = map(int, sys.stdin.readline().split())
x, y = x - 1, y - 1

for _ in range(m):
    passenger_y, passenger_x, dst_y, dst_x = map(int, sys.stdin.readline().split())
    passengers.add((passenger_x - 1, passenger_y - 1))
    destinations[(passenger_x - 1, passenger_y - 1)] = (dst_x - 1, dst_y - 1)

while True:
    passenger, dist = find_passenger(board, passengers, x, y)
    if fuel <= dist or passenger is None:
        fuel = -1
        break
    fuel -= dist
    x, y = passenger
    passengers.remove(passenger)

    dest = destinations[(x, y)]
    dist = calc_destination_dist(board, x, y, dest[0], dest[1])
    if fuel < dist or dist == -1:
        fuel = -1
        break
    fuel += dist
    x, y = dest

    if len(passengers) == 0:
        break

print(fuel)
