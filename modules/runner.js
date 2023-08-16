import { Worker } from "worker_threads";

console.defaultTimeEnd = console.timeEnd;
console.timeEnd = function (label) {
	let capturedOutput;
	let originalLog = console.log;

	console.log = (...args) => (capturedOutput = args[2]);
	console.defaultTimeEnd.call(console, label);

	console.log = originalLog;

	return capturedOutput;
};

function formatSolution(solution) {
	return `
	const { parentPort, workerData } = require("worker_threads");

	console.defaultLog = console.log;

	function BlockLog(stream) {
		console.log = (...args) => {
			stream.push(args);
		};
	}
	function UnBlockLog() {
		console.log = console.defaultLog;
	}
	
	${solution.toString()}

	try {
		let stream = [];
		BlockLog(stream);
		const output = solution(workerData.input);
		UnBlockLog();
		parentPort.postMessage({output, stream});
	} finally {
		UnBlockLog();
	}
	`;
}

export async function run(solution, tc, i) {
	return new Promise((resolve, reject) => {
		console.time(i);
		const worker = new Worker(formatSolution(solution), {
			eval: true,
			workerData: { input: tc.input },
		});

		worker.on("message", ({ output, stream }) => {
			resolve({
				input: tc.input,
				expected: tc.output,
				output: output,
				passed: JSON.stringify(output) === JSON.stringify(tc.output),
				time: console.timeEnd(i),
				stream: stream,
			});
		});
		worker.on("error", (err) => {
			console.timeEnd(i);
			reject({
				input: tc.input,
				expected: tc.output,
				err: err,
			});
		});
		worker.on("exit", (code) => {
			if (code !== 0)
				reject(new Error(`Worker stopped with exit code ${code}`));
		});
	});
}
