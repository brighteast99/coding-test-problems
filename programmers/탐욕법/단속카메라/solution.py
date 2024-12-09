def solution(routes):
    routes.sort(key=lambda route: route[1])
    cameras = 0
    last = -30001
    for [entry, exit] in routes:
        if entry > last:
            cameras += 1
            last = exit
    return cameras
