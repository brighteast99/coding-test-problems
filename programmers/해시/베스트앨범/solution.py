def solution(genres, plays):
    genre_statistics = dict()

    for i, (genre, n_played) in enumerate(zip(genres, plays)):
        if genre in genre_statistics:
            genre_statistics[genre]["plays"] += n_played
            genre_statistics[genre]["musics"].append(i)
        else:
            genre_statistics[genre] = {"plays": n_played, "musics": [i]}

    genre_names = list(genre_statistics.keys())
    genre_names.sort(key=lambda name: -genre_statistics[name]["plays"])
    answer = []
    for genre in genre_names:
        genre_statistics[genre]["musics"].sort(key=lambda num: (-plays[num], num))
        answer.extend(genre_statistics[genre]["musics"][:2])

    return answer
