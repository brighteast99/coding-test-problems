def solution(grid):
    UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3
    dir_delta = {
        UP: (0, -1),
        DOWN: (0, 1),
        LEFT: (-1, 0),
        RIGHT: (1, 0)
    }
    next_dir = {
        UP: {
            "S": UP,
            "L": LEFT,
            "R": RIGHT
        },
        DOWN: {
            "S": DOWN,
            "L": RIGHT,
            "R": LEFT,
        },
        LEFT: {
            "S": LEFT,
            "L": DOWN,
            "R": UP
        },
        RIGHT: {
            "S": RIGHT,
            "L": UP,
            "R": DOWN
        }
    }
    width, height = len(grid[0]), len(grid)
    visited = [[[False, False, False, False]
                for __ in range(width)] for _ in range(height)]

    answer = []
    for y in range(height):
        for x in range(width):
            for dir in [UP, DOWN, LEFT, RIGHT]:
                cur_x, cur_y, cur_dir, path_len = x, y, dir, 0
                while not visited[cur_y][cur_x][cur_dir]:
                    visited[cur_y][cur_x][cur_dir] = True
                    path_len += 1
                    cur_x = (cur_x + dir_delta[cur_dir][0]) % width
                    cur_y = (cur_y + dir_delta[cur_dir][1]) % height
                    cur_dir = next_dir[cur_dir][grid[cur_y][cur_x]]

                if path_len:
                    answer.append(path_len)

    return sorted(answer)
