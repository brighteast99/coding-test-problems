function solution(n, vertex) {
  let graph = Array.from({ length: n }, () => new Set())
  vertex.forEach(([a, b]) => {
    graph[a - 1].add(b - 1)
    graph[b - 1].add(a - 1)
  })

  let visited = new Set([0])
  let distances = Array.from({ length: n }, () => null)
  let queue = [0]
  distances[0] = 0
  while (queue.length) {
    let current = queue.shift()

    graph[current].forEach(node => {
      if (visited.has(node)) return
      distances[node] = distances[current] + 1
      queue.push(node)
      visited.add(node)
    })
  }

  const maxDist = Math.max(...distances)
  return distances.filter(dist => dist === maxDist).length
}
