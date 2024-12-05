def solution(array, commands):
    return list(
        map(
            lambda command: sorted(array[command[0] - 1 : command[1]])[command[2] - 1],
            commands,
        )
    )
