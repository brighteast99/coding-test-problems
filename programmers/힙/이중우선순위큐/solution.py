def solution(operations):
    pq = []

    for operation in operations:
        [command, arg] = operation.split(' ')
        arg = int(arg)

        if command == 'I':
            pq.append(arg)
            pq.sort()
        elif command == 'D' and len(pq) > 0:
            if arg == 1:
                pq.pop()
            elif arg == -1:
                pq.pop(0)

    return [pq[-1], pq[0]] if len(pq) > 0 else [0, 0]
