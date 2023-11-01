function solution(book_time) {
  book_time = book_time
    .map(times => {
      return times.map(time =>
        time.split(':').reduce((accum, curr) => accum * 60 + Number(curr), 0)
      )
    })
    .sort((a, b) => a[0] - b[0])
  console.log(book_time)
  let rooms = [book_time.shift()[1] + 10]

  while (book_time.length) {
    const [start, end] = book_time.shift()
    let idx = null
    for (let i = 0; i < rooms.length; i++) if (rooms[i] <= start) idx = i

    if (idx !== null) rooms[idx] = end + 10
    else rooms.push(end + 10)
  }

  return rooms.length
}
