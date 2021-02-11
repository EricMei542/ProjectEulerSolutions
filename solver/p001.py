# Find the sum of all the multiples of 3 or 5 below 1000
def compute(n: int) -> int:
	return sum([x for x in range(n) if x % 3 == 0 or x % 5 == 0])


if __name__ == '__main__':
	n = 10
	print(compute(n))