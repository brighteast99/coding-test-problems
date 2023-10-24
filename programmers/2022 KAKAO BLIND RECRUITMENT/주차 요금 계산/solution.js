function calcFee(fees, minutes) {
  const [threshold, minimumFee, unitTime, unitFee] = fees
  let fee = 0

  minutes -= threshold
  fee += minimumFee
  if (minutes <= 0) return minimumFee

  fee += Math.ceil(minutes / unitTime) * unitFee

  return fee
}

function toMinutes(time) {
  let [hour, minute] = time.split(':').map(val => parseInt(val))
  return hour * 60 + minute
}

function solution(fees, records) {
  let logs = {}
  records.forEach(record => {
    let [time, num, _] = record.split(' ')
    logs[num] ??= []
    logs[num].push(time)
  })

  return Object.keys(logs)
    .sort((a, b) => parseInt(a) - parseInt(b))
    .map(num => {
      let timestamps = logs[num]
      let accum = 0
      for (let i = 0; i < timestamps.length; i += 2)
        accum +=
          toMinutes(timestamps[i + 1] || '23:59') - toMinutes(timestamps[i])

      return calcFee(fees, accum)
    })
}
