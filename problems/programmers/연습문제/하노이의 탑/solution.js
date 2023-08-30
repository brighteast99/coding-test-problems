function move(n, from, by, to, moves) {
  if (n === 1) {
    moves.push([from, to])
    return
  }
  move(n - 1, from, to, by, moves)
  moves.push([from, to])
  move(n - 1, by, from, to, moves)
}

function solution({ n }) {
  var answer = []

  move(n, 1, 2, 3, answer)

  return answer
}
