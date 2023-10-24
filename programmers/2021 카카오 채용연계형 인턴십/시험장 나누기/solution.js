function dfs(num, links, sizeLimit, groupsLimit, root) {
  let temp = [root]
  let postOrder = []
  let cuts = 0

  while (temp.length) {
    let top = temp.pop()
    postOrder.push(top)

    if (links[top][0] != -1) temp.push(links[top][0])
    if (links[top][1] != -1) temp.push(links[top][1])
  }

  while (postOrder.length) {
    if (cuts >= groupsLimit) return false
    let curr = postOrder.pop()
    let groupSize = num[curr]
    let [left, right] = links[curr]

    let leftSize = num[left] ?? 0
    let rightSize = num[right] ?? 0

    if (groupSize + leftSize + rightSize <= sizeLimit) {
      num[curr] = groupSize + leftSize + rightSize
    } else if (
      groupSize + leftSize > sizeLimit &&
      groupSize + rightSize > sizeLimit
    ) {
      cuts += 2
    } else if (groupSize + leftSize > sizeLimit) {
      num[curr] = groupSize + rightSize
      cuts += 1
    } else if (groupSize + rightSize > sizeLimit) {
      num[curr] = groupSize + leftSize
      cuts += 1
    } else {
      num[curr] = groupSize + Math.min(leftSize, rightSize)
      cuts += 1
    }
  }

  return cuts < groupsLimit
}

function solution(k, num, links) {
  let isChild = new Array(num.length).fill(false)
  links.forEach(([left, right]) => {
    isChild[left] = true
    isChild[right] = true
  })
  let root = isChild.findIndex(x => !x)

  let left = Math.max(...num)
  let right = num.reduce((accum, curr) => accum + curr)
  while (left <= right) {
    let mid = Math.floor((left + right) / 2)
    if (dfs([...num], links, mid, k, root)) right = mid - 1
    else left = mid + 1
  }

  return left
}
