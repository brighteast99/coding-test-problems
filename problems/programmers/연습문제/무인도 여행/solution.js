function dfs(map, size, x, y) {
	if (!map[y]?.[x]?.days) return 0;
	if (map[y][x].visited) return 0;

	map[y][x].visited = true;

	return (
		map[y][x].days +
		dfs(map, size, x - 1, y) +
		dfs(map, size, x + 1, y) +
		dfs(map, size, x, y - 1) +
		dfs(map, size, x, y + 1)
	);
}

function solution({ maps }) {
	let islands = [];
	let size = {
		x: maps[0].length,
		y: maps.length,
	};
	console.log(size);
	let map = maps.map((map) =>
		Array.from(map).map((v) => {
			return {
				days: parseInt(v) || 0,
				visited: false,
			};
		})
	);

	for (let y = 0; y < size.y; y++)
		for (let x = 0; x < size.x; x++) {
			const island = dfs(map, size, x, y);
			if (island) islands.push(island);
		}

	if (!islands.length) return [-1];
	return islands.sort((a, b) => a - b);
}
