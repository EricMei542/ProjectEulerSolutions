# Find the largest palindrome made from the product of two 3-digit numbers
def compute() -> int:
    largest_palindrome = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            n = str(i * j)
            # palindrome ?
            if n == n[::-1]:
                largest_palindrome = max(int(n), largest_palindrome)

    return largest_palindrome


if __name__ == '__main__':
    print(compute())