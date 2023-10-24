function solution(operations) {
  let pq = []

  operations.forEach(op => {
    let [cmd, arg] = op.split(' ')
    arg = parseInt(arg)

    if (cmd === 'I') {
      pq.push(arg)
      pq.sort((a, b) => a - b)
    } else if (cmd === 'D' && pq.length) {
      if (arg === 1) pq.pop()
      else pq.shift()
    }
  })

  return pq.length ? [pq.pop(), pq.shift()] : [0, 0]
}
