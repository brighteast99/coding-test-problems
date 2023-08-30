import fs from 'fs'
import path from 'path'

export function initSolution(problemPath) {
  if (fs.existsSync(problemPath)) throw new Error('Problem already exists')

  fs.mkdirSync(problemPath, { recursive: true })

  let files = fs.readdirSync('./problems/template/')
  files.forEach(file => {
    const filePath = path.join('./problems/template/', file)
    const destFilePath = path.join(problemPath, file)
    fs.copyFileSync(filePath, destFilePath)
  })
}
