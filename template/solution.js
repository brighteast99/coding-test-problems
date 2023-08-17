function solution({ arg1, arg2 }) {
	let answer = "unexpected output";

	if (Math.floor(Math.random() * 2)) answer = "expected output";

	return answer;
}
