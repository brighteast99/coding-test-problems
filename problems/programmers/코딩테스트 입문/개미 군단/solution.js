function solution({ hp }) {
  let answer = 0

  for (let atk = 5; atk > 0; atk -= 2) {
    answer += Math.floor(hp / atk)
    hp = hp % atk
  }

  return answer
}
