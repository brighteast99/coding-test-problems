def solution(keymap, targets):
    key_dict = {}
    for key in keymap:
        for i in range(len(key)):
            char = key[i]
            if char not in key_dict or i + 1 < key_dict[char]:
                key_dict[char] = i + 1

    answer = []
    for string in targets:
        keystrokes = 0
        impossible = False
        for char in string:
            if char not in key_dict:
                impossible = True
                break
            keystrokes += key_dict[char]

        if impossible:
            answer.append(-1)
        else:
            answer.append(keystrokes)

    return answer
