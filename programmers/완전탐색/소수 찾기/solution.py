import itertools


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def solution(numbers: str):
    numbers = [numbers[i] for i in range(len(numbers))]
    primes = set()
    for l in range(1, len(numbers) + 1):
        for permutation in itertools.permutations(numbers, l):
            n = int("".join(permutation))
            if is_prime(n):
                primes.add(n)

    return len(primes)
