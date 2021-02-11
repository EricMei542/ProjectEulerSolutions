# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
import eulerlib

def compute(n: int) -> int:
    prime_factor_dict = {}
    for i in range(2, n + 1):
        prime_factors = eulerlib.prime_factors(i)
        for prime_factor in prime_factors:
            prime_factor_cnt = prime_factors.count(prime_factor)
            
            if prime_factor not in prime_factor_dict:
                prime_factor_dict[prime_factor] = 1
           
            elif prime_factor_dict[prime_factor] < prime_factor_cnt:
                prime_factor_dict[prime_factor] = prime_factor_cnt

    ans = 1
    for prime_factor, cnt in prime_factor_dict.items():
        ans *= prime_factor ** cnt

    return ans

if __name__ == '__main__':
    n = 20
    print(compute(n))