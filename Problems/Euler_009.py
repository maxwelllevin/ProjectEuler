# -*- coding: utf-8 -*-
"""
Euler #9
Pythagorean Triplet for which a + b + c = 1000 and a^2 + b^2 = c^2

Created on Tue Sep  5 21:04:56 2017

@author: Maxwell
"""


def make_perfect_squares(limit=100, square_list=[]):
	""" Return a list of perfect squares under the given limit """
	# Initialize our counter variable
	i = 2
	square_list.append(1)

	# Fill our square_list
	while square_list[-1] < limit:
		square_list.append(i * i)
		i += 1

	# Discard the last element if it is over our limit
	if square_list[-1] > limit:
		square_list.remove(square_list[-1])

	# Return our list
	return square_list


def find_pythagorean_triplets(square_limit=1000000):
	""" Returns a list containing lists of pythagorean triplets """
	# Create a list of perfect squares and a list to store our triplets
	square_list = make_perfect_squares(square_limit)
	pythag_triplets = []

	# Find the length of our list of squares so we can avoid repeating computations
	square_length = len(square_list)

	# Loop through our list without repeating elements
	# Note: this method works for this because we know square_list is sorted
	# and because we require c is largest square
	for a_index in range(square_length - 3 - 1):
		a = square_list[a_index]
		for b_index in range(a_index, square_length - 2 - 1):
			b = square_list[b_index]
			for c_index in range(b_index, square_length - 1 - 1):
				c = square_list[c_index]
				if a + b == c:
					pythag_triplets.append([int(a**0.5), int(b**0.5), int(c**0.5)])

	# Return our pythagorean triplets
	pythag_triplets.sort()
	return pythag_triplets


def add_pythag_list(pythag_triplets=[], sum_value=1000):
	""" Returns a list of triplets which satisfy a + b + c = sum_value"""
	# Create a list to contain triplets and triplet solutions
	pythag_triplets = find_pythagorean_triplets()
	solutions = []

	# Loop through our pythag_triplets list and look for solutions
	for trip_list in pythag_triplets:
		if trip_list[0] + trip_list[1] + trip_list[2] == sum_value:
			solutions.append(trip_list)

	# Return our list of solutions, should have just 1 list for sum_value = 1000
	return solutions


# ======= Compute the answer using our functions ======== #


# Import datetime so we can loosely track the (in)efficiency of our program
import datetime

before = datetime.datetime.today()

# Compute and print the solution to Euler #9
solution = add_pythag_list()
print("The Pythagorean triplet which satisfies Euler #9 is:", solution)

for a_list in solution:
	product = 1
	for item in a_list:
		product *= item

print("The product of this triplet is:", product)

# Compute and print time elapsed
after = datetime.datetime.today()
time_elapsed = after - before
print("Time elapsed during this computation:", time_elapsed)
