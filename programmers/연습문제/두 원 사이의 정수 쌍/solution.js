function solution(r1, r2) {
  let axis = r2 - r1 + 1
  let quadrant = 0

  for (let x = 1; x < r2; x++) {
    let y2 = Math.floor(Math.sqrt(r2 ** 2 - x ** 2))
    let y1 =
      x <= r1 ? Math.floor(Math.sqrt(Math.max(0, r1 ** 2 - x ** 2 - 1))) : 0
    quadrant += y2 - y1
  }

  return (axis + quadrant) * 4
}
