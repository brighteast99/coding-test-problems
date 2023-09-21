function solution(n, computers) {
  let networks = 0
  let unlinked = new Set(new Array(n).fill(null).map((_, i) => i))

  const graph = computers.map((linksFrom, i) => {
    let links = new Set()
    linksFrom.forEach((linkedTo, j) => {
      if (i !== j && linkedTo) links.add(j)
    })
    return links
  })

  while (unlinked.size) {
    let cur = Array.from(unlinked)[0]
    unlinked.delete(cur)

    let queue = [cur]
    let visited = new Set([cur])
    while (queue.length) {
      let next = queue.shift()

      graph[next].forEach(neighbor => {
        if (visited.has(neighbor)) return

        unlinked.delete(neighbor)
        visited.add(neighbor)
        queue.push(neighbor)
      })
    }
    networks++
  }

  return networks
}
