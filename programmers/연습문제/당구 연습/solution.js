function solution(m, n, startX, startY, balls) {
  return balls.map(([bx, by]) => {
    return Math.min(
      startX === bx && startY < by
        ? Number.MAX_SAFE_INTEGER
        : (bx - startX) ** 2 + (2 * n - (startY + by)) ** 2,
      startX === bx && by < startY
        ? Number.MAX_SAFE_INTEGER
        : (bx - startX) ** 2 + (startY + by) ** 2,
      startY === by && bx < startX
        ? Number.MAX_SAFE_INTEGER
        : (startX + bx) ** 2 + (by - startY) ** 2,
      startY === by && startX < bx
        ? Number.MAX_SAFE_INTEGER
        : (2 * m - (startX + bx)) ** 2 + (by - startY) ** 2
    )
  })
}
