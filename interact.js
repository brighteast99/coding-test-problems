import inquirer from 'inquirer'
import inquirerPrompt from 'inquirer-autocomplete-prompt'
inquirer.registerPrompt('autocomplete', inquirerPrompt)
import fs from 'fs'
import ora from 'ora'
import chalk from 'chalk'
chalk.orange = chalk.hex('#ffa500')
import { test, initSolution } from './actions/index.js'

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
        value: { path: fullPath, type: 'Run' },
        lastModified: fs.statSync(fullPath).mtime
      })
    })
  })
})
problems.sort((a, b) => b.lastModified - a.lastModified)
spinner.stop()

let { task, verbose, caseSelection, confirmAdd, source, category } =
  await inquirer.prompt([
    {
      name: 'task',
      type: 'autocomplete',
      message: 'Problem name to test or add:',
      source: (_, input) => {
        return new Promise(resolve => {
          if (!input) return resolve(problems)

          const filtered = problems.filter(problem =>
            problem.name
              .toLocaleLowerCase()
              .includes(input?.normalize('NFC').toLocaleLowerCase())
          )
          if (filtered.length) return resolve(filtered)
          else
            return resolve([
              {
                name: chalk.green(`Add new problem '${input}'`),
                value: { name: input, type: 'Add' }
              }
            ])
        })
      },
      loop: false
    },
    {
      name: 'verbose',
      type: 'list',
      message: 'Verbose:',
      when: ({ task }) => task.type === 'Run',
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
      type: 'confirm',
      message: 'Select test case?',
      when: ({ task }) => task.type === 'Run',
      default: false
    },
    {
      name: 'caseSelection',
      message: 'Choose cases to test: ',
      when: ({ task, selectCase }) => task.type === 'Run' && selectCase,
      type: 'checkbox',
      choices: ({ task }, input) => {
        const testCases = JSON.parse(
          fs.readFileSync(task.path + 'testCases.json', 'utf8')
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
    },
    {
      name: 'confirmAdd',
      type: 'confirm',
      message: ({ task }) => `Add new problem ${task.name}?`,
      when: ({ task }) => task.type === 'Add',
      default: true
    },
    {
      name: 'source',
      type: 'autocomplete',
      message: 'Problem from:',
      when: ({ task, confirmAdd }) => task.type === 'Add' && confirmAdd,
      source: async (_, input) => {
        return new Promise(resolve => {
          const sources = fs
            .readdirSync('./problems', { withFileTypes: true })
            .filter(
              dirent => dirent.isDirectory() && dirent.name !== 'template'
            )
            .map(dirent => dirent.name.normalize('NFC'))
          const filtered = sources.filter(source =>
            source.toLowerCase().includes(input?.normalize('NFC').toLowerCase())
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
      when: ({ task, confirmAdd }) => task.type === 'Add' && confirmAdd,
      source: ({ source }, input) => {
        return new Promise(resolve => {
          const categories = fs.existsSync(`./problems/${source}`)
            ? fs
                .readdirSync(`./problems/${source}`, { withFileTypes: true })
                .filter(
                  dirent => dirent.isDirectory() && dirent.name !== 'template'
                )
                .map(dirent => dirent.name.normalize('NFC'))
            : []
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
    }
  ])

if (task.type === 'Run') {
  const solutionFile = task.path + 'solution.js'
  const testCasesFile = task.path + 'testCases.json'
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
} else {
  if (source && category && task.name) {
    source = source.trim().replace('/', '∕')
    category = category.trim().replace('/', '∕')
    task.name = task.name.trim().replace('/', '∕')
    const spinner = ora('Setting up new problem...').start()
    initSolution(`./problems/${source}/${category}/${task.name}/`)
    spinner.succeed(
      `A new problem ${chalk.green(task.name)} is added under ${chalk.blue(
        './problems/' + source + '/' + category + '/'
      )}.`
    )
  }
}
