def solution(survey, choices):
    answer = ''
    scores = {'R': 0, 'T': 0,
              'C': 0, 'F': 0,
              'J': 0, 'M': 0,
              'A': 0, 'N': 0}

    for i in range(len(survey)):
        choice = choices[i] - 4
        if choice == 0:
            continue

        scores[survey[i][0 if choice < 0 else 1]] += abs(choice)

    answer += 'T' if scores['T'] > scores['R'] else 'R'
    answer += 'F' if scores['F'] > scores['C'] else 'C'
    answer += 'M' if scores['M'] > scores['J'] else 'J'
    answer += 'N' if scores['N'] > scores['A'] else 'A'

    return answer
