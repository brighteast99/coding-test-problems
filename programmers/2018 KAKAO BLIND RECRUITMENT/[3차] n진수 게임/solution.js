function solution(n, t, m, p) {
  let stream = ''

  for (let i = 0; stream.length < m * t + p - 1; i++) stream += i.toString(n)

  return stream
    .substring(0, m * (t - 1) + p)
    .toUpperCase()
    .split('')
    .filter((_, i) => i % m === p - 1)
    .join('')
}
