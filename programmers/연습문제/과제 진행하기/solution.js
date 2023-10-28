function solution(plans) {
  let answer = []
  plans = plans
    .map(([name, start, estimated]) => {
      return {
        name,
        startTime: start
          .split(':')
          .map(Number)
          .reduce((acc, cur) => acc * 60 + cur),
        estimatedTime: Number(estimated)
      }
    })
    .sort((a, b) => a.startTime - b.startTime)
  let stack = []

  while (plans.length) {
    const plan = plans.shift()

    if (!plans.length) {
      answer.push(plan.name)
      answer.push(...stack.map(p => p.name).reverse())
      break
    }

    const availableTime = plans[0].startTime - plan.startTime
    if (availableTime >= plan.estimatedTime) {
      answer.push(plan.name)
      if (stack.length) {
        let planToContinue = stack.pop()
        planToContinue.startTime = plan.startTime + plan.estimatedTime
        plans.unshift(planToContinue)
      }
    } else {
      plan.estimatedTime -= availableTime
      stack.push(plan)
    }
  }
  return answer
}
