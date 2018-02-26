# -*- coding: utf-8 -*-
"""
Euler #3
Finding the largest prime factor of 600851475143 

Created on Fri Sep  1 17:43:47 2017

@author: Maxwell

"""

# TODO: Fix for large numbers that exceed max recur. depth


prime_factors = []


def recursive_factor_to_prime(number, divisor=2):
	""" Uses recursion to iterate through integers under number and test for divisibility. Because it starts low,
	only primes will divide the number. Non-prime numbers will quickly pass by (hopefully) """
	if number % divisor == 0:
		number /= divisor
		prime_factors.append(divisor)
		factor_to_prime(number, divisor)
	elif divisor < number:
		factor_to_prime(number, divisor + 1)
	elif divisor == number:
		prime_factors.append(divisor)


def factor_to_prime(number):
	""" Returns the largest prime factor of a given number. """
	divisor = 2
	while divisor != number:
		if number % divisor == 0:
			number /= divisor
			prime_factors.append(divisor)
		else:
			divisor += 1
	prime_factors.append(int(number))
	return number


print(factor_to_prime(600851475143))
