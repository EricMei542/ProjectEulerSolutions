# What is the largest prime factor of the number 600851475143?
import eulerlib

def compute(n: int) -> int:
    return max(eulerlib.prime_factors(n))


if __name__ == '__main__':
    n = 600851475143
    print(compute(n))