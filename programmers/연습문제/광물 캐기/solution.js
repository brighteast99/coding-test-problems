function sum(...numbers) {
  return numbers.reduce((acc, cur) => acc + cur, 0)
}

function solution(picks, minerals) {
  picks = picks
    .map((count, i) => new Array(count).fill(Math.pow(5, 2 - i)))
    .flat()

  minerals = minerals.map(mineral => {
    switch (mineral) {
      case 'diamond':
        return 25
      case 'iron':
        return 5
      case 'stone':
        return 1
      default:
        return null
    }
  })
  let mineralGroups = []

  for (let i = 0; i < picks.length; i++)
    if (minerals.length) mineralGroups.push(minerals.splice(0, 5))

  return sum(
    ...mineralGroups
      .sort((a, b) => sum(...b) - sum(...a))
      .reduce(
        (accum, group, i) =>
          accum + sum(...group.map(mineral => Math.max(mineral / picks[i], 1)))
      )
      .flat()
  )
}
