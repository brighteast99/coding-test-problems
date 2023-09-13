const SHEEP = 0
const WOLF = 1

function canTake(info, n, sheeps, wolves) {
  if (info[n] === SHEEP) return true
  return wolves < sheeps - 1
}

function scanDistToSheep(info, childInfo, n, nodeInfo) {
  if (info[n] === undefined) return { dist: 100, sheeps: 0 }

  nodeInfo[n] =
    info[n] === SHEEP ? { dist: 0, sheeps: 1 } : { dist: 100, sheeps: 0 }

  childInfo[n].forEach(child => {
    let { dist, sheeps } = scanDistToSheep(info, childInfo, child, nodeInfo)
    nodeInfo[n].dist = Math.min(nodeInfo[n].dist, dist + 1)
    nodeInfo[n].sheeps += sheeps
  })

  return nodeInfo[n]
}

function comp(nodeInfo, sheeps, wolves, a, b) {
  let reachable = [
    nodeInfo[a].dist < sheeps - wolves,
    nodeInfo[b].dist < sheeps - wolves
  ]

  if (reachable[0] && reachable[1]) {
    return (
      nodeInfo[b].sheeps - nodeInfo[a].sheeps ||
      nodeInfo[a].dist - nodeInfo[b].dist
    )
  } else if (reachable[0]) return -1
  else if (reachable[1]) return 1
  else return 0
}

function solution(info, edges) {
  let heads = [0]
  let nodeInfo = new Array(info.length)
  let childInfo = Array.from({ length: info.length }, () => [])
  edges.forEach(([from, to]) => childInfo[from].push(to))
  scanDistToSheep(info, childInfo, 0, nodeInfo)

  let sheeps = 0
  let wolves = 0

  let allStuck
  do {
    allStuck = true
    for (let i = 0; i < heads.length; i++) {
      if (nodeInfo[heads[i]].dist >= 100) {
        heads.splice(i--, 1)
        continue
      }

      let stuck = !canTake(info, heads[i], sheeps, wolves)
      allStuck &&= stuck

      if (stuck) continue
      else {
        info[heads[i]] === SHEEP ? sheeps++ : wolves++
        heads.push(...childInfo[heads[i]])
        heads.splice(i, 1)
        heads.sort((a, b) => comp(nodeInfo, sheeps, wolves, a, b))
        break
      }
    }
  } while (!allStuck)

  return sheeps
}
