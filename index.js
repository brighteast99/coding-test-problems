import chalk from 'chalk'
import { program } from 'commander'
import fs from 'fs'
import { Runner } from './modules/runner.js'
import { printResult, printTestReport } from './modules/printer.js'

async function test(solutionFile, testCases, options) {
  const report = {
    total: testCases.length,
    pass: 0,
    fail: 0,
    error: 0
  }

  const runner = new Runner(solutionFile)

  await runner.init()
  Promise.all(
    testCases.map((tc, i) =>
      runner
        .run(tc, i)
        .then(result => {
          if (result.passed) report.pass++
          else report.fail++

          if (!options.reportOnly) printResult(i, result, options.silent)
        })
        .catch(result => {
          report.error++
          if (!options.reportOnly) printResult(i, result, options.silent)
        })
    )
  ).then(() => printTestReport(report))
}

program.version('1.0.0').description('Simple code runner')
import chalk from "chalk";
import fs from "fs";
import { program } from "commander";
import { test } from "./actions/index.js";

program.description("Simple code runner");

program
  .command('run <solution-path>')
  .option('-s --silent')
  .option('-r --report-only')
  .description('Run solution file with test cases')
  .action(async (solutionPath, options) => {
    if (!solutionPath.endsWith('/')) solutionPath += '/'
    const solutionFile = solutionPath + 'solution.js'
    const testCasesFile = solutionPath + 'testCases.json'
	.command("test <solution-path>")
	.option("-s --silent")
	.option("-r --report-only")
	.description("Test the solution function with the given test cases.")
	.action(async (solutionPath, options) => {
		if (!solutionPath.endsWith("/")) solutionPath += "/";
		const solutionFile = solutionPath + "solution.js";
		const testCasesFile = solutionPath + "testCases.json";

    if (!fs.existsSync(solutionFile) || !fs.existsSync(testCasesFile)) {
      console.error(chalk.red('Solution not found'))
      process.exit(1)
    }
    fs.readFile(testCasesFile, 'utf8', (err, data) => {
      try {
        if (err) throw err
		if (!fs.existsSync(solutionFile) || !fs.existsSync(testCasesFile)) {
			console.error(chalk.red("Solution file or test cases are not found"));
			process.exit(1);
		}
		fs.readFile(testCasesFile, "utf8", (err, data) => {
			try {
				if (err) throw err;

        const testCases = JSON.parse(data)
        test(solutionFile, testCases, options)
      } catch (err) {
        console.error(chalk.red('Failed to read test cases'))
        console.error(chalk.red(err))
        process.exit(1)
      }
    })
  })

program.parse(process.argv)
