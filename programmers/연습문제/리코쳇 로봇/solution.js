const ROAD = '.'
const WALL = 'D'
const START = 'R'
const GOAL = 'G'

function isWall(board, x, y) {
  return ![ROAD, START, GOAL].includes(board[y]?.[x])
}

function Node(x, y) {
  return `(${x}, ${y})`
}

function solution(board) {
  let start, goal
  for (let row of board) {
    let _start = row.indexOf(START)
    if (_start != -1) {
      start = [_start, board.indexOf(row)]
    }
    let _goal = row.indexOf(GOAL)
    if (_goal != -1) {
      goal = [_goal, board.indexOf(row)]
    }

    if (start !== undefined && goal !== undefined) break
  }

  let movesNeeded = {}
  let queue = [start]
  movesNeeded[Node(...start)] = 0

  while (queue.length) {
    let [x, y] = queue.shift()
    let cur = Node(x, y)

    if (x === goal[0] && y === goal[1]) return movesNeeded[cur]

    for (let dy = y - 1; dy >= -1; dy--)
      if (isWall(board, x, dy)) {
        if (movesNeeded[Node(x, dy + 1)] == null) {
          movesNeeded[Node(x, dy + 1)] = movesNeeded[cur] + 1
          queue.push([x, dy + 1])
        }
        break
      }
    for (let dy = y + 1; dy <= board.length; dy++)
      if (isWall(board, x, dy)) {
        if (movesNeeded[Node(x, dy - 1)] == null) {
          movesNeeded[Node(x, dy - 1)] = movesNeeded[cur] + 1
          queue.push([x, dy - 1])
        }
        break
      }
    for (let dx = x - 1; dx >= -1; dx--)
      if (isWall(board, dx, y)) {
        if (movesNeeded[Node(dx + 1, y)] == null) {
          movesNeeded[Node(dx + 1, y)] = movesNeeded[cur] + 1
          queue.push([dx + 1, y])
        }
        break
      }
    for (let dx = x + 1; dx <= board[0].length; dx++)
      if (isWall(board, dx, y)) {
        if (movesNeeded[Node(dx - 1, y)] == null) {
          movesNeeded[Node(dx - 1, y)] = movesNeeded[cur] + 1
          queue.push([dx - 1, y])
        }
        break
      }
  }

  return -1
}
