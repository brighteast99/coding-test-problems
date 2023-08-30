import { Runner } from '../modules/runner.js'
import { printResult, printTestReport } from '../modules/printer.js'

export async function test(solutionFile, testCases, options) {
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
