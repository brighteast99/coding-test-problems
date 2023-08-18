/**
 * let {a, b} = sides && a > b
 * The length of the 3rd side x must satisfy (a - b + 1 <= x < a + b)
 */
function solution({ sides }) {
	return 2 * (sides[0] < sides[1] ? sides[0] : sides[1]) - 1;
}
