function solution(priorities, location) {
  let answer = 0
  for (; location >= 0; location--) {
    const current = priorities.shift()
    if (Math.max(...priorities) > current) {
      priorities.push(current)
      if (location === 0) {
        location = priorities.length
      }
    } else answer += 1
  }

  return answer
}
