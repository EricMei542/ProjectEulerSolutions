# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
def compute(n: int) -> int:
	fibonacci = [1 ,2]
	ans = 0
	while fibonacci[-1] < n:
		if fibonacci[-1] % 2 == 0:
			ans += fibonacci[-1]
		fibonacci.append(fibonacci[-1] + fibonacci[-2])
	return ans


if __name__ == '__main__':
	n = 4000000
	print(compute(n))