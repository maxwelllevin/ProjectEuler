# -*- coding: utf-8 -*-
"""
Euler #12: Highly Divisible Triangle Number

Created on Sat Sep 23 20:04:31 2017

@author: Maxwell
"""

from collections import Counter


def get_triangle(n):
	""" Returns the nth triangle number. """
	return n * (n + 1) / 2


def prime_factors(num):
	""" Return a dict of prime factors, counts of a number. """
	hist = Counter()
	div = 2
	while num != 1:
		if num % div == 0:
			num /= div
			hist[div] += 1
		else:
			div += 1
	return dict(hist)


def count_divisors(num):
	""" Returns the number of divisors of a given number. """
	factors = 1
	hist = prime_factors(num)
	for key in hist:
		factors *= hist[key] + 1
	return factors


def first_triangle_number(divisors, start=1):
	""" Returns the first triangle number to have more than the specified number of divisors. """
	tri = get_triangle(start)
	while count_divisors(tri) <= divisors:
		start += 1
		tri = get_triangle(start)
	return tri


if __name__ == '__main__':
	print(first_triangle_number(500))
