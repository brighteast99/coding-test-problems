function findNetwork(wires, network) {
	if (!network.length) {
		network.push(...wires.pop());
		return findNetwork(wires, network);
	}

	let target = wires.findIndex(
		([from, to]) => network.includes(from) || network.includes(to)
	);
	if (target != -1) {
		if (network.includes(wires[target][0])) network.push(wires[target][1]);
		else network.push(wires[target][0]);
		wires.splice(target, 1);

		return findNetwork(wires, network);
	} else return network;
}

function solution({ n, wires }) {
	var answer = n;

	for (let cut = 0; cut < wires.length; cut++) {
		let network = findNetwork(
			wires.slice(0, cut).concat(wires.slice(cut + 1)),
			[]
		);

		answer = Math.min(answer, Math.abs(network.length - (n - network.length)));
	}

	return answer;
}
