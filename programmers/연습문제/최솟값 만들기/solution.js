function solution(A, B) {
  A.sort((a, b) => a - b)
  B.sort((a, b) => b - a)

  return A.reduce((accum, cur, idx) => accum + cur * B[idx], 0)
}
