function canTransform(from, to) {
  return from.split('').filter((char, i) => char !== to.charAt(i)).length == 1
}

function solution(begin, target, words) {
  let visited = {}
  let queue = [begin]
  visited[begin] = 0

  while (queue.length) {
    let cur = queue.shift()
    if (cur === target) return visited[cur]

    words
      .filter(word => !visited[word] && canTransform(cur, word))
      .forEach(node => {
        visited[node] = visited[cur] + 1
        queue.push(node)
      })
  }

  return 0
}
