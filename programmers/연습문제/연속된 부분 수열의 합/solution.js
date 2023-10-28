function sum(...numbers) {
  return numbers.reduce((accum, cur) => accum + cur)
}

function solution(sequence, k) {
  let left = 0
  let right = 0
  let sum = sequence[0]

  let answers = []
  while (right < sequence.length) {
    if (sum === k) answers.push([left, right])
    if (sum < k) {
      right++
      sum += sequence[right]
    } else {
      if (left === right) {
        right++
        sum += sequence[right]
      }
      sum -= sequence[left]
      left++
    }
  }

  answers.sort((a, b) => a[1] - a[0] - (b[1] - b[0]))

  return answers[0]
}
