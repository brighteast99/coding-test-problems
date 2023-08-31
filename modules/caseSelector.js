function maskString(string, start, end, maskWith) {
  if (!end) end = start

  if (start >= string.length) return string
  if (end >= string.length) end = string.length - 1

  return (
    string.slice(0, start) +
    maskWith.repeat(end - start + 1) +
    string.slice(end + 1)
  )
}

export function select(tc, option) {
  if (!option) return tc

  let mask = '1'.repeat(tc.length)
  const regex = /(\d+)(?:-(\d+))?|\^(\d+)(?:-(\d+))?/

  option.split(',').forEach((o, i) => {
    const match = o.match(regex)

    if (match) {
      if (!i && (match[1] || match[2])) mask = mask.replaceAll('1', '0')

      if (match[1])
        mask = maskString(mask, parseInt(match[1]), parseInt(match[2]), '1')
      else if (match[3])
        mask = maskString(mask, parseInt(match[3]), parseInt(match[4]), '0')
    }
  })

  return tc.filter((_, i) => mask[i] === '1')
}
