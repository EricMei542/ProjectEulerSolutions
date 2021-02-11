# What is the 10001st prime number?
import eulerlib


def compute(n: int) -> int:

    primes = []
    current = 2

    while len(primes) < n:
        while not eulerlib.is_prime(current):
            current += 1

        primes.append(current)
        current += 1

    return primes[-1]

if __name__ == '__main__':
    n = 10001
    print(compute(n))