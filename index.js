import chalk from 'chalk'
import fs from 'fs'
import { program } from 'commander'
import { test, initSolution } from './actions/index.js'

program.description('Simple code runner')

program
  .command('test <solution-path>')
  .option('-s --silent')
  .option('-r --report-only')
  .option('-t, --case-selection <caseSelection>')
  .description('Test the solution function with the given test cases.')
  .action(async (solutionPath, options) => {
    if (!solutionPath.endsWith('/')) solutionPath += '/'
    const solutionFile = solutionPath + 'solution.js'
    const testCasesFile = solutionPath + 'testCases.json'

    if (!fs.existsSync(solutionFile) || !fs.existsSync(testCasesFile)) {
      console.error(chalk.red('Solution file or test cases are not found'))
      process.exit(1)
    }
    fs.readFile(testCasesFile, 'utf8', (err, data) => {
      try {
        if (err) throw err

        const testCases = JSON.parse(data)
        test(solutionFile, testCases, options)
      } catch (err) {
        console.error(chalk.red('Failed to read test cases'))
        console.error(chalk.red(err))
        process.exit(1)
      }
    })
  })

program
  .command('create <problem-name>')
  .option('-f --from <problem-from>', 'Where you found the problem', 'unknown')
  .option('-c --category <category>', 'Problem category', 'unclassified')
  .description('Create files for new problem using template')
  .action((problemName, { from, category }) => {
    try {
      initSolution(`./problems/${from}/${category}/${problemName}/`)
    } catch (err) {
      console.error(chalk.red(err))
      process.exit(1)
    }
  })

program.parse(process.argv)
