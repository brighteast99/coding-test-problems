def convert_date(date):
    [year, month, date] = list(map(int, date.split('.')))
    return (year - 2000) * 12 * 28 + (month - 1) * 28 + date

def solution(today, terms, privacies):
    answer = []
    term_dict = {}

    today = convert_date(today)

    for term in terms:
        [type, duration] = term.split(' ')
        term_dict[type] = int(duration)

    for i in range(len(privacies)):
        [date, type] = privacies[i].split(' ')
        date = convert_date(date)

        if date + term_dict[type] * 28 <= today:
            answer.append(i+1)

    return answer
