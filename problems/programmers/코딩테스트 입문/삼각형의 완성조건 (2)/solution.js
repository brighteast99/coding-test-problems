function solution({ sides }) {
	return 2 * (sides[0] < sides[1] ? sides[0] : sides[1]) - 1;
}
