function mark(board, x, y) {
	for (let dx = -1; dx <= 1; dx++)
		for (let dy = -1; dy <= 1; dy++)
			if (board[y + dy]?.[x + dx] === 0) board[y + dy][x + dx] = 2;
}

function solution({ board }) {
	for (let y = 0; y < board.length; y++)
		for (let x = 0; x < board[y].length; x++)
			if (board[y][x] === 1) mark(board, x, y);

	return board.reduce(
		(accum, curr) => accum + curr.filter((x) => !x).length,
		0
	);
}
