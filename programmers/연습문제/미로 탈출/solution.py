START = 'S'
EXIT = 'E'
LEVER = 'L'
PATH = 'O'
WALL = 'X'


class Pos:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __repr__(self):
        return f'({self.x}, {self.y})'

    def north(self, dist: int = 1):
        return Pos(self.x, self.y - dist)

    def east(self, dist: int = 1):
        return Pos(self.x + dist, self.y)

    def south(self, dist: int = 1):
        return Pos(self.x, self.y + dist)

    def west(self, dist: int = 1):
        return Pos(self.x - dist, self.y)


def bfs(maps, visited, start: Pos, destination):
    queue = [(start, 0)]
    (rows, cols) = (len(maps), len(maps[0]))

    while len(queue) > 0:
        (cur, time) = queue.pop(0)

        if cur.x < 0 or cur.x >= cols or cur.y < 0 or cur.y >= rows or \
                visited[cur.y][cur.x] or \
                maps[cur.y][cur.x] == WALL:
            continue

        visited[cur.y][cur.x] = True

        if maps[cur.y][cur.x] == destination:
            return time

        queue.extend([(cur.north(), time + 1), (cur.east(), time + 1), (cur.south(), time + 1), (cur.west(), time + 1)])

    return -1


def solution(maps):
    (rows, cols) = (len(maps), len(maps[0]))

    for row in range(rows):
        if START in maps[row]:
            start = Pos(maps[row].find(START), row)

        if LEVER in maps[row]:
            lever = Pos(maps[row].find(LEVER), row)

    to_lever = bfs(maps, [[False] * cols for _ in range(rows)], start, LEVER)
    if to_lever == -1:
        return -1
    to_exit = bfs(maps, [[False] * cols for _ in range(rows)], lever, EXIT)
    if to_exit == -1:
        return -1

    return to_lever + to_exit
