function solution(targets) {
  targets.sort((a, b) => a[1] - b[1])

  let answer = 1
  let pos = targets.shift()[1] - 0.5
  for (let target of targets) {
    if (target[0] < pos && pos < target[1]) continue
    answer++
    pos = target[1] - 0.5
  }

  return answer
}
