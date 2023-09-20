function dfs(numbers, target, index, sum) {
  if (index === numbers.length) {
    return Number(sum === target)
  }
  return (
    dfs(numbers, target, index + 1, sum + numbers[index]) +
    dfs(numbers, target, index + 1, sum - numbers[index])
  )
}

function solution(numbers, target) {
  return dfs(numbers, target, 0, 0)
}
