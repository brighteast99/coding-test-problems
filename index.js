import chalk from "chalk";
import { program } from "commander";
import fs from "fs";
import { run } from "./modules/runner.js";
import { printResult, printTestReport } from "./modules/printer.js";

function test(solution, TC, options) {
	const report = {
		pass: 0,
		fail: 0,
		error: 0,
	};

	Promise.all(
		TC.map((tc, i) =>
			run(solution, tc, i)
				.then((result) => {
					if (result.passed) report.pass++;
					else report.fail++;

					if (!options.reportOnly) printResult(i, result, options.silent);
				})
				.catch((result) => {
					report.error++;
					if (!options.reportOnly) printResult(i, result, options.silent);
				})
		)
	).then(() => printTestReport(report));
}

program.version("1.0.0").description("Simple code runner");

program
	.command("run <filePath>")
	.option("-s --silent")
	.option("-r --report-only")
	.description("Run solution file with test cases")
	.action(async (filePath, options) => {
		if (!fs.existsSync(filePath)) {
			console.log(chalk.red(`Solution file not found: ${file}`));
			process.exit(1);
		}

		import(filePath).then(({ solution, TC }) => {
			test(solution, TC, options);
		});
	});

program.parse(process.argv);
