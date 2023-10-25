function solution(progresses, speeds) {
  const daysNeeded = progresses.map((progress, idx) =>
    Math.ceil((100 - progress) / speeds[idx])
  )

  return daysNeeded.reduce(
    (() => {
      let start = null
      let features = 0
      return (acc, cur, idx) => {
        if (start === null) {
          start = cur
          features = 1
        } else if (cur > start) {
          acc.push(features)
          start = cur
          features = 1
        } else features++

        if (idx === daysNeeded.length - 1) acc.push(features)

        return acc
      }
    })(),
    []
  )
}
