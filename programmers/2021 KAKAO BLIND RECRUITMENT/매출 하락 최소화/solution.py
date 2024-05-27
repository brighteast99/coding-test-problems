def team_min_cost(sales, team, teams):
    if not isinstance(team, dict):
        return [0, sales[team - 1]]

    crew_min = 0
    crew_all_absent = 0
    candidate = 2**31 -1
    for crew in team['crews']:
        [crew_present, crew_absent] = team_min_cost(sales, teams[crew] if crew in teams else crew, teams)
        crew_min += min(crew_absent, crew_present)
        crew_all_absent += crew_absent
        candidate = min(candidate, crew_present - crew_absent)

    leader_present = sales[team['leader'] - 1] + crew_min
    leader_absent = crew_min

    if (leader_absent == crew_all_absent):
        leader_absent += candidate

    return [leader_present, leader_absent]


def solution(sales, links):
    teams = {}

    for [leader, crew] in links:
        if leader not in teams:
            teams[leader] = { 'leader': leader, 'crews': [] }
        teams[leader]['crews'].append(crew)

    return min(team_min_cost(sales, teams[1], teams))
