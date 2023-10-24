function solution(cards) {
  let states = cards.map(() => false)
  let groupSizes = []

  while (states.some(state => !state)) {
    let groupSize = 0
    for (
      let pos = states.indexOf(states.find(state => !state));
      !states[pos];
      pos = cards[pos] - 1
    ) {
      groupSize += 1
      states[pos] = true
    }
    groupSizes.push(groupSize)
  }

  groupSizes.sort((a, b) => b - a)
  if (groupSizes.length < 2) return 0
  return groupSizes[0] * groupSizes[1]
}
