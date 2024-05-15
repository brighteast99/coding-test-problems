def solution(data, ext, val_ext, sort_by):
    map_column = {
        "code": 0,
        "date": 1,
        "maximum": 2,
        "remain": 3
    }

    return list(sorted(filter(lambda row: row[map_column[ext]] < val_ext, data),
                key=lambda data: data[map_column[sort_by]]))
