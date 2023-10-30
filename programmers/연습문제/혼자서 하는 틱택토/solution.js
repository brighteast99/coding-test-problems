function hasLine(board, player) {
  if (board.some(row => Array.from(row).every(col => col === player)))
    return true
  if ([0, 1, 2].some(idx => board.every(row => row[idx] === player)))
    return true
  if (board.every((row, i) => row[i] === player)) return true
  if (board.every((row, i) => row[2 - i] === player)) return true
  return false
}

function solution(board) {
  let o = 0
  let x = 0

  board.forEach(row =>
    Array.from(row).forEach(col => {
      if (col === 'O') o++
      else if (col === 'X') x++
    })
  )

  const oMade = hasLine(board, 'O')
  const xMade = hasLine(board, 'X')
  if (o > x + 1 || o < x || (oMade && xMade)) return 0
  if (oMade) return o === x + 1 ? 1 : 0
  if (xMade) return o === x ? 1 : 0
  return 1
}
