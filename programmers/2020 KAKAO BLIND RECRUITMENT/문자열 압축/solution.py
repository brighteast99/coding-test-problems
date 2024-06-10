def solution(s):
    answer = len(s)

    for chunk_size in range(1, int(len(s) // 2 + 1)):
        compressed_len = len(s)
        last_chunk = ''
        redundant_chunks = 0
        for i in range(0, len(s) + 1, chunk_size):
            cur_chunk = s[i : i + chunk_size]

            if cur_chunk == last_chunk:
                redundant_chunks += 1
                continue

            last_chunk = cur_chunk
            if redundant_chunks > 0:
                compressed_len += len(str(redundant_chunks + 1))
                compressed_len -= redundant_chunks * chunk_size
                redundant_chunks = 0

        answer = min(answer, compressed_len)

    return answer
