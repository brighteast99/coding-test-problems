import chalk from "chalk";

export function printResult(i, result, silent) {
	console.log("====================================================");
	console.log(
		(result.err || !result.passed ? chalk.red : chalk.green)(`테스트 ${i + 1}`)
	);

	console.log("----------------------------------------------------");
	if (result.err) {
		console.log(`입력값: ${JSON.stringify(result.input)}`);
		if (!silent) {
			console.error(chalk.red(result.err.stack));
		} else console.error(chalk.red(result.err.message));
	} else {
		console.log(`   입력값: ${JSON.stringify(result.input)}`);
		console.log(`   기댓값: ${result.expected}`);
		console.log(
			`실행 결과: ${
				result.passed
					? chalk.green("정답")
					: chalk.red(`오답 (${result.output})`)
			}`
		);
		console.log(`실행 시간: ${result.time}`);
		if (!silent) {
			console.log("----------------------------------------------------");
			console.log("출력");
			result.stream.forEach((log) => console.log(...log));
		}
	}
	console.log("====================================================");
	console.log();
}

export function printTestReport(report) {
	console.log("====================================================");
	console.log("테스트 결과");
	console.log("----------------------------------------------------");
	console.log(
		`정답: ${(!report.fail && !report.error ? chalk.green : chalk.red)(
			report.pass
		)}, 오답: ${(report.fail ? chalk.red : chalk.green)(
			report.fail
		)}, 오류: ${(report.error ? chalk.red : chalk.green)(report.error)}\n`
	);
	console.log(
		`결과: ${
			!report.fail && !report.error
				? chalk.green("테스트 통과!")
				: chalk.red("테스트 실패")
		}`
	);
	console.log("====================================================");
}
