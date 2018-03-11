# -*- coding: utf-8 -*-
"""
Euler #14
Longest Collatz Sequence

Created on Sat Mar 10 2018

@author: Maxwell
"""

# Use a python dictionary to implement caching for seen
# key = number in sequence, value = distance from 1
seen = {1: 1, 2: 2}

# len_at_start keeps track of just the lengths of the starting values we've seen
len_at_start = {1: 1, 2: 2}


def collatz_length(n):
	""" Returns the integer length of the collatz sequence starting at n. """
	visited = []
	num = n
	while num != 1:
		if num in seen:
			visited += [num]
			break
		else:
			visited += [num]

		if num % 2 == 0:
			num /= 2
		else:
			num = 3 * num + 1

	# Update Seen
	visited = visited[::-1]
	start = seen[visited[0]]
	for i in range(len(visited)):
		seen[visited[i]] = start + i

	# Update len_at_start
	len_at_start[n] = seen[n]
	return seen[n]


def longest_collatz():
	""" Returns the length of the longest Collatz Sequence under 1,000,000."""
	n = 2
	while n < 1000000:
		collatz_length(n)
		n += 1
	return max(len_at_start, key=len_at_start.get)


print(longest_collatz())
