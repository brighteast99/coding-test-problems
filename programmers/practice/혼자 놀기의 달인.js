export const TC = [
	{
		input: [8, 6, 3, 7, 2, 5, 1, 4],
		output: 12,
	},
	{
		input: [5, 3, 2, 1, 4],
		output: 6,
	},
	{
		input: [1, 2],
		output: 1,
	},
	{
		input: [2, 1],
		output: 0,
	},
	{
		input: [1, 5, 3, 2, 4],
		output: 3,
	},
];

export function solution(cards) {
	let states = cards.map(() => false);
	let groupSizes = [];

	while (states.some((state) => !state)) {
		let groupSize = 0;
		for (
			let pos = states.indexOf(states.find((state) => !state));
			!states[pos];
			pos = cards[pos] - 1
		) {
			groupSize += 1;
			states[pos] = true;
		}
		console.log(groupSize);
		groupSizes.push(groupSize);
	}

	groupSizes.sort((a, b) => b - a);
	if (groupSizes.length < 2) return 0;
	return groupSizes[0] * groupSizes[1];
}
