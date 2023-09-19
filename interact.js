import inquirer from 'inquirer'
import inquirerPrompt from 'inquirer-autocomplete-prompt'
import fs from 'fs'
import ora from 'ora'
import chalk from 'chalk'
chalk.orange = chalk.hex('#ffa500')

import { test, initSolution } from './actions/index.js'

inquirer.registerPrompt('autocomplete', inquirerPrompt)

const { task } = await inquirer.prompt({
  name: 'task',
  type: 'list',
  message: 'Choose action:',
  choices: [
    { name: 'Run tests', value: 'test' },
    { name: 'Add new problem', value: 'create' },
    new inquirer.Separator(),
    { name: chalk.red('Exit'), value: 'exit' }
  ]
})

switch (task) {
  case 'test': {
    const spinner = ora('Loading problem list...').start()
    const problems = []

    fs.readdirSync('./problems', { withFileTypes: true }).forEach(source => {
      if (!source.isDirectory() || source.name === 'template') return

      fs.readdirSync(`./problems/${source.name}`, {
        withFileTypes: true
      }).forEach(category => {
        if (!category.isDirectory()) return

        fs.readdirSync(`./problems/${source.name}/${category.name}`, {
          withFileTypes: true
        }).forEach(problem => {
          if (!problem.isDirectory()) return

          const fullPath = `./problems/${source.name}/${category.name}/${problem.name}/`
          problems.push({
            name: problem.name.normalize('NFC'),
            value: fullPath,
            lastModified: fs.statSync(fullPath).mtime
          })
        })
      })
    })
    problems.sort((a, b) => b.lastModified - a.lastModified)
    spinner.stop()

    const { solutionPath, verbose, caseSelection } = await inquirer.prompt([
      {
        name: 'solutionPath',
        type: 'autocomplete',
        message: 'Problem to test:',
        source: (_, input) => {
          return new Promise(resolve => {
            resolve(
              input
                ? problems.filter(problem =>
                    problem.name
                      .toLocaleLowerCase()
                      .includes(input?.toLocaleLowerCase())
                  )
                : problems
            )
          })
        },
        emptyText: chalk.orange(`No result`),
        validate: choice =>
          !!choice || chalk.red(`Select problem that exists.`),
        loop: false
      },
      {
        name: 'verbose',
        type: 'list',
        message: 'Verbose:',
        choices: [
          {
            name: `3 ${chalk.gray('(All logs)')}`,
            value: 3
          },
          {
            name: `2 ${chalk.gray('(Errors only)')}`,
            value: 2
          },
          {
            name: `1 ${chalk.gray('(Results only)')}`,
            value: 1
          },
          {
            name: `0 ${chalk.gray('(Reports only)')}`,
            value: 0
          }
        ],
        default: 0
      },
      {
        name: 'selectCase',
        message: 'Select test case?',
        type: 'confirm',
        default: false
      },
      {
        name: 'caseSelection',
        message: 'Choose cases to test: ',
        when: ({ selectCase }) => selectCase,
        type: 'checkbox',
        choices: ({ solutionPath }, input) => {
          const testCases = JSON.parse(
            fs.readFileSync(solutionPath + 'testCases.json', 'utf8')
          )
          return testCases.map((testCase, index) => {
            return {
              name: `${index + 1}) ${
                JSON.stringify(testCase.input).substring(0, 20) + '...'
              }`,
              value: index,
              checked: true
            }
          })
        },
        validate: input => {
          return (
            !!input.length ||
            chalk.red('You should choose at least one test case.')
          )
        }
      }
    ])

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
        test(solutionFile, testCases, {
          verbose: verbose,
          caseSelection: caseSelection
        })
      } catch (err) {
        console.error(chalk.red('Failed to read test cases'))
        console.error(chalk.red(err))
        process.exit(1)
      }
    })
    break
  }
  case 'create': {
    const spinner = ora('Loading info...').start()
    const categoriesBySource = fs
      .readdirSync('./problems', { withFileTypes: true })
      .filter(dirent => dirent.isDirectory() && dirent.name !== 'template')
      .reduce((acc, dirent) => {
        return {
          ...acc,
          [dirent.name.normalize('NFC')]: fs
            .readdirSync(`./problems/${dirent.name}`, { withFileTypes: true })
            .filter(dirent => dirent.isDirectory())
            .map(dirent => dirent.name.normalize('NFC'))
        }
      }, {})
    spinner.stop()

    let { source, category, problemName } = await inquirer.prompt([
      {
        name: 'source',
        type: 'autocomplete',
        message: 'Problem from:',
        source: async (_, input) => {
          return new Promise(resolve => {
            const sources = Object.keys(categoriesBySource)
            const filtered = sources.filter(source =>
              source
                .toLowerCase()
                .includes(input?.normalize('NFC').toLowerCase())
            )

            if (filtered.length) return resolve(filtered)
            if (sources.length && !input) return resolve(sources)
            if (input)
              return resolve([
                {
                  name: chalk.green(`From new source "${input}"`),
                  value: input.normalize('NFC')
                }
              ])
            return resolve([
              {
                name: chalk.orange(
                  `No sources registered now.\nType a name for new source.`
                ),
                noInput: true
              }
            ])
          })
        },
        validate: choice => {
          if (typeof choice === 'object' && choice.noInput)
            return chalk.red('Source is required')

          return true
        },
        loop: false
      },
      {
        name: 'category',
        type: 'autocomplete',
        message: 'Problem related to:',
        source: ({ source }, input) => {
          return new Promise(resolve => {
            const categories = categoriesBySource[source] || []
            const filtered = categories.filter(category =>
              category
                .toLowerCase()
                .includes(input?.normalize('NFC').toLowerCase())
            )
            if (filtered.length) return resolve(filtered)
            if (categories.length && !input) return resolve(categories)
            if (input)
              return resolve([
                {
                  name: chalk.green(`New category "${input}"`),
                  value: input.normalize('NFC')
                }
              ])
            return resolve([
              {
                name: chalk.orange(
                  `No categories registered in ${source} now.\nType a name for new category.`
                ),
                noInput: true
              }
            ])
          })
        },
        validate: choice => {
          if (typeof choice === 'object' && choice.noInput)
            return chalk.red('Category is required')

          return true
        },
        loop: false
      },
      {
        name: 'problemName',
        type: 'input',
        message: 'Problem name:',
        when: ({ source, category }) => source && category,
        validate: (input, { source, category }) => {
          if (!fs.existsSync(`./problems/${source}/${category}`)) return true

          let problems = fs
            .readdirSync(`./problems/${source}/${category}`, {
              withFileTypes: true
            })
            .filter(dirent => dirent.isDirectory())
            .map(dirent => dirent.name.normalize('NFC'))
          if (problems.includes(input.normalize('NFC')))
            return chalk.red('Problem already exists')
          return true
        }
      }
    ])

    if (source && category && problemName) {
      source = source.trim().replace('/', '∕')
      category = category.trim().replace('/', '∕')
      problemName = problemName.trim().replace('/', '∕')
      const spinner = ora('Setting up new problem...').start()
      initSolution(`./problems/${source}/${category}/${problemName}/`)
      spinner.succeed(
        `A new problem ${chalk.green(problemName)} is added under ${chalk.blue(
          './problems/' + source + '/' + category + '/'
        )}.`
      )
    }
    break
  }
  case 'exit':
    console.log(chalk.red('Exit program'))
    break
  default:
    break
}
