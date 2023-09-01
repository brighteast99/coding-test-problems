function solution(s) {
  let open = 0

  for (let i = 0; i < s.length; i++) {
    const br = s[i] === '('
    if (br) open += 1
    else {
      if (!open) return false
      open -= 1
    }
  }

  return !open
}
