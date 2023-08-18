function isSquared(n) {
	let sqrt = Math.pow(n, 0.5);
	return sqrt === Math.floor(sqrt);
}

function solution({ left, right }) {
	answer = 0;

	for (let i = left; i <= right; i++) {
		answer += (isSquared(i) ? -1 : 1) * i;
	}

	return answer;
}
