function solution({ n, words }) {
	var answer = [0, 0];
	let dict = {};

	dict[words[0]] = true;
	let last = words[0].slice(-1);
	for (let i = 1; i < words.length; i++) {
		if (dict[words[i]] || words[i].slice(0, 1) != last) {
			answer[0] = (i % n) + 1;
			answer[1] = parseInt(i / n) + 1;
			break;
		}

		last = words[i].slice(-1);
		dict[words[i]] = true;
	}

	return answer;
}
