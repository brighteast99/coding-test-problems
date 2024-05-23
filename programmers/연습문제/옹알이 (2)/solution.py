def can_pronounce(word):
    BABBLINGS = ['aya', 'ye', 'woo', 'ma']
    last = None

    while len(word):
        pronouncable = False
        for BABBLING in BABBLINGS:
            if word.startswith(BABBLING) and BABBLING != last:
                last = BABBLING
                word = word[len(BABBLING):]
                pronouncable = True

        if not pronouncable:
            return False

    return True


def solution(babbling):
    answer = 0

    for word in babbling:
        if can_pronounce(word):
            answer += 1

    return answer
