function solution({ wallpaper }) {
	const FILE = "#";
	let answer = {
		lux: null,
		luy: wallpaper[0].length,
		rdx: 0,
		rdy: 0,
	};

	wallpaper.forEach((curr, i) => {
		if (!curr.includes(FILE)) return;

		answer.lux = answer.lux ?? i;
		answer.rdx = i + 1;
		const first = curr.indexOf(FILE);
		const last = curr.lastIndexOf(FILE);
		if (first != -1 && first < answer.luy) answer.luy = first;
		if (last != -1 && last + 1 > answer.rdy) answer.rdy = last + 1;
	});

	return Object.values(answer);
}
