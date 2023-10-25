function primeFactorization(num) {
  let answer = {}

  for (let i = 2; i <= num; i++)
    if (num % i === 0) {
      answer[i] = (answer[i] || 0) + 1
      num /= i
      i--
    }

  return answer
}

function solution(arr) {
  const answerFactors = arr.reduce((acc, cur) => {
    let factors = primeFactorization(cur)
    for (const [key, value] of Object.entries(factors))
      acc[key] = Math.max(acc[key] || 0, value)

    return acc
  }, {})

  let answer = 1
  for (const [key, value] of Object.entries(answerFactors))
    answer *= Math.pow(key, value)

  return answer
}
