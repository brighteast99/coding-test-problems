import { Worker } from 'worker_threads'
import fs from 'fs'

console.defaultTimeEnd = console.timeEnd
console.timeEnd = function (label) {
  let capturedOutput
  let originalLog = console.log

  console.log = (...args) => (capturedOutput = args[2])
  console.defaultTimeEnd.call(console, label)

  console.log = originalLog

  return capturedOutput
}

export class Runner {
  constructor(solutionFile) {
    this.sourcePath = solutionFile
    this.source = 'source'
    this.args = []
  }

  async init() {
    return new Promise((resolve, reject) => {
      fs.promises
        .readFile(this.sourcePath, 'utf-8')
        .then(data => {
          this.args = data
            .match(/solution\((.*)\)/)[1]
            .split(',')
            .map(arg => arg.trim())
          this.source = `
    const { parentPort, workerData } = require("worker_threads");

    console.defaultLog = console.log;
    console.defaultDir = console.dir;
    console.defaultAssert = console.assert;
    console.defaultTable = console.table;

    function BlockLog(stream) {
        console.log = (...args) => {
            stream.push(
              {
                type: "log",
                data: JSON.stringify(args)
              });
        };
        console.dir = (...args) => {
          stream.push({
            type: "dir",
            data: JSON.stringify(args)
          });
        }
        console.assert = (...args) => {
          stream.push({
            type: "assert",
            data: JSON.stringify(args)
          });
        }
        console.table = (...args) => {
          stream.push({
            type: "table",
            data: JSON.stringify(args)
          });
        }
    }
    function UnBlockLog() {
        console.log = console.defaultLog;
        console.dir = console.defaultDir;
        console.assert = console.defaultAssert;
        console.table = console.defaultTable;
    }
    
    ${data}

	let stream = [];
    try {
        BlockLog(stream);
        const output = solution(...workerData.input);
        UnBlockLog();
        parentPort.postMessage({output, stream});
    } catch(err) {
		UnBlockLog();
		parentPort.postMessage({err:err, stream});
		// throw new Error(JSON.stringify({error: err, stream: stream}));
	}
    `
          resolve()
        })
        .catch(err => reject(err))
    })
  }

  async run(tc, i) {
    return new Promise((resolve, reject) => {
      console.time(i)
      const worker = new Worker(this.source, {
        eval: true,
        workerData: { input: this.args.map(arg => tc.input[arg]) }
      })

      worker.on('message', ({ err, output, stream }) => {
        let data = {
          input: tc.input,
          expected: tc.output,
          output: output,
          passed: JSON.stringify(output) === JSON.stringify(tc.output),
          time: console.timeEnd(i),
          stream: stream,
          err: err
        }
        return err ? reject(data) : resolve(data)
      })
      worker.on('exit', code => {
        if (code !== 0)
          reject(new Error(`Worker stopped with exit code ${code}`))
      })
    })
  }
}
