START = "S"
OBSTACLE = "X"


def solution(park, routes):
    valid_y = range(0, len(park))
    valid_x = range(0, len(park[0]))
    pos_y = 0
    pos_x = 0

    for i in valid_y:
        if START in park[i]:
            pos_y = i
            pos_x = park[i].index(START)
            break

    direction_vector = {
        "E": [0, 1],
        "W": [0, -1],
        "S": [1, 0],
        "N": [-1, 0]
    }

    for route in routes:
        [direction, distance] = route.split(" ")
        distance = int(distance)
        vector = direction_vector[direction]

        skip = False
        for i in range(1, distance + 1):
            check_y = pos_y + i * vector[0]
            check_x = pos_x + i * vector[1]

            if check_y not in valid_y or \
                    check_x not in valid_x or \
                    park[check_y][check_x] == OBSTACLE:
                skip = True
                break

        if skip:
            continue

        pos_y += vector[0] * distance
        pos_x += vector[1] * distance

    return [pos_y, pos_x]
