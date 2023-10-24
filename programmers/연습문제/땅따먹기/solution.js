function solution(land) {
  for (let row = 1; row < land.length; row++) {
    for (let col = 0; col < 4; col++) {
      land[row][col] += Math.max(
        ...land[row - 1].slice(0, col),
        ...land[row - 1].slice(col + 1)
      )
    }
  }

  return Math.max(...land[land.length - 1])
}
