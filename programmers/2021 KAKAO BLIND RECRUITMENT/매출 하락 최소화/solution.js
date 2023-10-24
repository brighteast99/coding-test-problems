function dfs(sales, team, teams) {
  if (typeof team !== 'object') return [0, sales[team - 1]]

  let subCosts = []
  let minSubCost = 0
  let allAbsent = 0
  let candidateCost = Number.MAX_SAFE_INTEGER
  team.crews.forEach(leader => {
    let temp = dfs(sales, teams[leader] || leader, teams)
    subCosts.push(temp)
    minSubCost += Math.min(...temp)
    allAbsent += temp[0]
    if (temp[1] - temp[0] < candidateCost) candidateCost = temp[1] - temp[0]
  })

  let leaderPresent = sales[team.leader - 1] + minSubCost
  let leaderAbsent = minSubCost
  if (leaderAbsent == allAbsent) leaderAbsent += candidateCost

  return [leaderAbsent, leaderPresent]
}
function solution(sales, links) {
  let teams = {}

  links.forEach(([leader, crew]) => {
    teams[leader] ??= { leader: leader, crews: [] }
    teams[leader].crews.push(crew)
  })

  return Math.min(...dfs(sales, teams[1], teams))
}
