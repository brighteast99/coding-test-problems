function preorder(node, log) {
	if (!node) return;

	log.push(node.value);
	preorder(node.left, log);
	preorder(node.right, log);
}

function postorder(node, log) {
	if (!node) return;

	postorder(node.left, log);
	postorder(node.right, log);
	log.push(node.value);
}

function constructTree(nodeinfo, parent, left, right) {
	if (!nodeinfo.length) return;

	let leftChild = nodeinfo.filter(
		(node) => left <= node.position.x && node.position.x < parent.position.x
	)?.[0];
	if (leftChild) {
		parent.left = leftChild;
		nodeinfo.splice(nodeinfo.indexOf(leftChild), 1);
		constructTree(nodeinfo, leftChild, left, parent.position.x - 1);
	}
	let rightChild = nodeinfo.filter(
		(node) => parent.position.x < node.position.x && node.position.x <= right
	)?.[0];
	if (rightChild) {
		parent.right = rightChild;
		nodeinfo.splice(nodeinfo.indexOf(rightChild), 1);
		constructTree(nodeinfo, rightChild, parent.position.x + 1, right);
	}
}

function solution({ nodeinfo }) {
	let answer = [[], []];
	nodeinfo = nodeinfo.map((node, idx) => {
		return {
			value: idx + 1,
			position: { x: node[0], y: node[1] }
		};
	});
	nodeinfo.sort((a, b) => {
		return b.position.y - a.position.y;
	});

	let tree = nodeinfo.splice(0, 1)[0];
	constructTree(nodeinfo, tree, 0, 100000);

	preorder(tree, answer[0]);
	postorder(tree, answer[1]);

	return answer;
}
