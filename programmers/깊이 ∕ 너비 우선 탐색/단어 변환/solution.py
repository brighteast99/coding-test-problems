def solution(begin, target, words):
    def transformable(word_from, word_to):
        return len([chr for idx, chr in enumerate(word_from) if word_to[idx] != chr]) == 1

    queue = [begin]
    distances = {begin: 0}
    while len(queue):
        cur = queue.pop()
        if cur == target:
            return distances[cur]

        for word in words:
            if word in distances or not transformable(cur, word):
                continue
            distances[word] = distances[cur] + 1
            queue.append(word)

    return 0
