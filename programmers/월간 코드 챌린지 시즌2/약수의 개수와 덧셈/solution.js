function solution(left, right) {
  return Array.from({ length: right - left + 1 }, (_, i) => left + i).reduce(
    (acc, cur) =>
      Number.isInteger(Math.pow(cur, 0.5)) ? acc - cur : acc + cur,
    0
  )
}
