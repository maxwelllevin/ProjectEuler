# -*- coding: utf-8 -*-
"""
Euler #5
Smallest multiple of all numbers from 1 to 20

Created on Mon Sep  4 21:01:54 2017

@author: Maxwell
"""

import datetime


def factor_to_prime(number):
	"""Returns a list containing the prime factorization of 'number' """
	prime_factors = []
	divisor = 2
	while divisor != number:
		if number % divisor == 0:
			number /= divisor
			prime_factors.append(divisor)
		else:
			divisor += 1
	prime_factors.append(int(number))
	return prime_factors


def combine_lists(a_list=[], b_list=[]):
	"""Returns a combination of two lists. Somewhat like a union, but for lists. Preserves the larger number of copies
	of an item between 2 lists. """
	new_list = a_list

	# If b_list has more copies of a specific item, copy excess to new_list
	for item in a_list:
		if b_list.count(item) > a_list.count(item):
			num_copy = b_list.count(item) - a_list.count(item)
			for copies_left in range(num_copy):
				new_list.append(item)

	# Copy the remaining elements of b_list to new_list
	for item in b_list:
		if a_list.count(item) == 0:
			num_copy = b_list.count(item)
			for copies_left in range(num_copy):
				new_list.append(item)

	new_list.sort()
	return new_list


def lcm_integers_under(limit=2):
	""" Returns a list containing the prime factors of the lcm of all positive integers under the given limit """
	lcm_factors = []
	for integers in range(2, limit):
		factored_int = factor_to_prime(integers)
		lcm_factors = combine_lists(lcm_factors, factored_int)
		factored_int.clear()
	lcm_factors.sort()
	return lcm_factors


def mult_through_list(mult_list):
	""" Returns the product of all the elements of a given list """
	product = 1
	for item in mult_list:
		product *= item
	return product


before = datetime.datetime.today()

lcm_list = lcm_integers_under(100)
print(lcm_list)

ans = mult_through_list(lcm_list)
print(ans)

after = datetime.datetime.today()
print(after - before)
