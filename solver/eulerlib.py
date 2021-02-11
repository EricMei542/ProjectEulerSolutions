import numpy as np
import math

def is_prime(n: int) -> bool:
    """Return if n is a prime number."""
    if n > 2 and n % 2 == 0:
        return False
    return n == 2 or np.all([n % x for x in range(3, int(np.sqrt(n)) + 1)])


def prime_factors(n: int) -> list:
    prime_factors_list = []
    for i in range(2,int(math.sqrt(n))+1):
        while n % i == 0: 
            n /= i
            prime_factors_list.append(i)

    if n > 2:
        prime_factors_list.append(n)
    return prime_factors_list
