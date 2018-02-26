# -*- coding: utf-8 -*-
"""
Euler #7
10,001st prime

Created on Tue Sep  5 19:37:47 2017

@author: Maxwell
"""

import datetime

prime_cache = []
prime_cache.append(2)


def is_prime(n, has_cache=False):
	"""Return True if 'n' is prime. False otherwise. 'has_cache'
		indicates use of caching in order to speed up prime solving"""
	# If we have cached the value, then return True
	if has_cache:
		if n in prime_cache:
			return True
		# Check our cache to see if our cache divides 'n'
		for divisor in prime_cache:
			if n % divisor == 0:
				return False

	# If nothing in our cache divides it, check manually if prime
	if not has_cache:
		for divisor in range(2, int(n**0.5 + 1)):
			if n % divisor == 0:
				return False
	return True


def find_n_prime(n):
	"""Returns the Nth prime"""
	if n == 1:
		return 2
	p = 3
	num_found = 1

	# Find primes until we've found the Nth prime
	while num_found < n:
		# When we find a prime increment num_found and cache it
		if is_prime(p, True):
			num_found += 1
			prime_cache.append(p)
		p += 2

	# Return the Nth prime when we've found 'N' primes
	if num_found == n:
		return p - 2


before = datetime.datetime.today()
print("The 10,001st prime is: ", find_n_prime(10001))
after = datetime.datetime.today()

time_elapsed = after - before
print("Time Elapsed = " + str(time_elapsed))
