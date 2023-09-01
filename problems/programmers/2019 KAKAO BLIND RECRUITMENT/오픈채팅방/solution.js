function solution(record) {
  let users = {}
  let answer = []

  for (let i = 0; i < record.length; i++) {
    let [, id, name] = record[i].split(' ')
    if (name) users[id] = name
  }

  for (let i = 0; i < record.length; i++) {
    let [type, id] = record[i].split(' ')
    switch (type) {
      case 'Enter':
        answer.push(`${users[id]}님이 들어왔습니다.`)
        break
      case 'Leave':
        answer.push(`${users[id]}님이 나갔습니다.`)
        break
      default:
        continue
    }
  }
  return answer
}
