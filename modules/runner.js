import { Worker } from "worker_threads";
import fs from "fs";

console.defaultTimeEnd = console.timeEnd;
console.timeEnd = function (label) {
	let capturedOutput;
	let originalLog = console.log;

	console.log = (...args) => (capturedOutput = args[2]);
	console.defaultTimeEnd.call(console, label);

	console.log = originalLog;

	return capturedOutput;
};

export class Runner {
	constructor(solutionFile) {
		this.sourcePath = solutionFile;
		this.source = "source";
	}

	async init() {
		return new Promise((resolve, reject) => {
			fs.promises
				.readFile(this.sourcePath, "utf-8")
				.then((data) => {
					this.source = `
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
    
    ${data}

	let stream = [];
    try {
        BlockLog(stream);
        const output = solution(workerData.input);
        UnBlockLog();
        parentPort.postMessage({output, stream});
    } catch(err) {
		UnBlockLog();
		parentPort.postMessage({err:err, stream});
		// throw new Error(JSON.stringify({error: err, stream: stream}));
	}
    `;
					resolve();
				})
				.catch((err) => reject(err));
		});
	}

	async run(tc, i) {
		return new Promise((resolve, reject) => {
			console.time(i);
			const worker = new Worker(this.source, {
				eval: true,
				workerData: { input: tc.input },
			});

			worker.on("message", ({ err, output, stream }) => {
				let data = {
					input: tc.input,
					expected: tc.output,
					output: output,
					passed: JSON.stringify(output) === JSON.stringify(tc.output),
					time: console.timeEnd(i),
					stream: stream,
					err: err,
				};
				return err ? reject(data) : resolve(data);
			});
			worker.on("exit", (code) => {
				if (code !== 0)
					reject(new Error(`Worker stopped with exit code ${code}`));
			});
		});
	}
}
