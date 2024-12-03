def solution(genres, plays):
    genre_statistics = dict()
    n_musics = len(genres)

    for i in range(n_musics):
        genre = genres[i]
        if genre in genre_statistics:
            genre_statistics[genre]["plays"] += plays[i]
            genre_statistics[genre]["musics"].append(i)
        else:
            genre_statistics[genre] = {"plays": plays[i], "musics": [i]}

    genre_names = genre_statistics.keys()
    genre_names.sort(key=lambda name: genre_statistics[name]["plays"], reverse=True)
    answer = []
    for genre in genre_names:
        genre_statistics[genre]["musics"].sort(key=lambda num: (plays[num], num))
        answer.extend(genre_statistics[genre]["musics"][:2])

    return answer
