function solution(n) {
  let answer = Array.from({ length: n }, (_, i) => new Array(i + 1).fill(0))

  let order = 1
  let cur = { x: 0, y: 0 }
  let dir = 0
  while (order <= (n * (n + 1)) / 2) {
    answer[cur.y][cur.x] = order

    if (dir === 0 && answer[cur.y + 1]?.[cur.x] != 0) dir = 1
    else if (dir === 1 && answer[cur.y][cur.x + 1] != 0) dir = 2
    else if (dir === 2 && answer[cur.y - 1]?.[cur.x - 1] != 0) dir = 0

    switch (dir) {
      case 0:
        cur.y++
        break
      case 1:
        cur.x++
        break
      case 2:
        cur.x--
        cur.y--
        break
      default:
    }

    order++
  }

  return answer.flat()
}
