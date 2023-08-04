# Problem Statement
# https://www.hackerrank.com/contests/projecteuler/challenges/euler004/problem

# Youtube link for explanation
# https://youtu.be/phAhR3dYJRQ

import math

def get_factors(N):
	factors = []
	for number in range(1, int(math.sqrt(N) + 1)):
		if N % number == 0:
			factors.append(number)
			factors.append(N // number)
	return factors

for _ in range(int(input())):
	n= int(input())
	factors = get_factors(n)
	# print(factors)
	largest_prime_factor = 1
	for factor in factors:
		if factor > largest_prime_factor:
			f = get_factors(factor)
			if len(f) == 2:
				largest_prime_factor = factor
	print(largest_prime_factor)
