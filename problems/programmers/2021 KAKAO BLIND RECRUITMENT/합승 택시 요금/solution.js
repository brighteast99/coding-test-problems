function solution(n, s, a, b, fares) {
  const INF = Number.MAX_SAFE_INTEGER
  let answer = INF

  const costs = Array.from({ length: n }, (_, i) => {
    let temp = new Array(n).fill(INF)
    temp[i] = 0
    return temp
  })
  fares.forEach(([from, to, cost]) => {
    costs[from - 1][to - 1] = cost
    costs[to - 1][from - 1] = cost
  })

  for (let by = 0; by < n; by++)
    for (let from = 0; from < n; from++)
      for (let to = 0; to < n; to++)
        costs[from][to] = Math.min(
          costs[from][to],
          costs[from][by] + costs[by][to]
        )

  for (let middle = 0; middle < n; middle++)
    answer = Math.min(
      answer,
      costs[s - 1][middle] + costs[middle][a - 1] + costs[middle][b - 1]
    )

  return answer
}
