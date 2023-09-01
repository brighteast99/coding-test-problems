function canBuild(a, b, g, s, w, t, T) {
  let [S, G, total] = [0, 0, 0]

  t.forEach((t, i) => {
    let W = Math.min(g[i] + s[i], w[i] * Math.round(T / (2 * t)))

    S += Math.min(s[i], W)
    G += Math.min(g[i], W)
    total += W
  })

  return a <= G && b <= S && a + b <= total
}

function solution(a, b, g, s, w, t) {
  let left = 1
  let right = Math.max(...t) * (a + b) * 2

  while (left <= right) {
    let mid = Math.floor((left + right) / 2)

    if (canBuild(a, b, g, s, w, t, mid)) right = mid - 1
    else left = mid + 1
  }

  return left
}
