# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def compute(n: int) -> int:

    sum_of_the_square = sum([x ** 2 for x in range(1, n + 1)])
    square_of_the_sum = ((n * (n + 1)) / 2) ** 2

    return square_of_the_sum - sum_of_the_square

if __name__ == '__main__':
    n = 100
    print(compute(n))