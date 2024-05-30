def handle_sharp(code):
        if '#' not in code:
            return code

        code = list(code)
        for i in range(len(code)):
            if code[i] == '#':
                code[i-1] = code[i-1].lower()

        code = [c for c in code if c != '#']
        return ''.join(code)


def solution(m, musicinfos):
    m = handle_sharp(m)

    matches = []
    for idx, music_info in enumerate(musicinfos):
        [start, end, title, code] = music_info.split(',')

        [start_hour, start_min] = map(int, start.split(':'))
        [end_hour, end_min] = map(int, end.split(':'))
        duration = (end_hour - start_hour) * 60 + end_min - start_min

        code = handle_sharp(code)

        played_code = code * (duration // len(code)) + code[:duration % len(code)]
        if m in played_code:
            matches.append({'title': title, 'duration': duration})

    if len(matches) == 0:
        return '(None)'

    matches.sort(key=lambda match: -match['duration'])
    return matches[0]['title']
