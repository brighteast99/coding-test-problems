def solution(s, skip, index):
    skip = list(map(lambda char: ord(char), skip))

    answer = []
    for i in range(len(s)):
        char = ord(s[i])

        shifted = 0
        while shifted < index:
            char += 1
            if char > ord('z'):
                char = ord('a')

            if char in skip:
                continue

            shifted += 1

        answer.append(chr(char))

    return ''.join(answer)