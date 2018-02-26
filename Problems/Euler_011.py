# -*- coding: utf-8 -*-
"""
Euler #11
Largest product of 4 digits in a grid (up, down, left, right, or diagonal)

Created on Thu Sep  7 16:24:53 2017

@author: Maxwell
"""


def make_grid_from_file(filepath, euler_grid=[[]]):
	""" Returns the grid we'll be using for this problem
		from a file I've named euler_11_input.txt """
	# Open the file
	file = open(filepath, 'r')

	# Grab input from file
	i = 0
	for line in file:
		for num in line.split():
			euler_grid[i].append(int(num))
		euler_grid.append([])
		i += 1

	# Print the file
	for i in range(20):
		print(euler_grid[i])

	# Close the file and return our data as a grid
	file.close()
	return euler_grid


def row_test(grid, cycle=4):
	""" Returns the greatest product of (cycle) numbers in any row. """
	maxprod = 1
	numcol = len(grid[0])
	numrow = len(grid) - 1

	for i in range(numrow):
		for j in range(numcol - cycle):
			product = 1
			for p in range(cycle):
				product *= grid[i][j + p]
			if maxprod < product:
				maxprod = product
	return maxprod


def column_test(grid, cycle=4):
	# Returns the greatest product of (cycle) numbers in any column
	maxprod = 1
	numcol = len(grid[0])
	numrow = len(grid) - 1

	for i in range(numrow - cycle):
		for j in range(numcol):
			product = 1
			for p in range(cycle):
				product *= grid[i + p][j]
			if maxprod < product:
				maxprod = product
	return maxprod


def diag_1(grid, cycle=4):
	# Returns the largest product of 4 numbers from lower left to top right
	maxprod = 1
	numcol = len(grid[0])
	numrow = len(grid) - 1

	for i in range(cycle - 1, numrow):
		for j in range(numcol - cycle):
			product = 1
			for p in range(cycle):
				product *= grid[i - p][j + p]
			if maxprod < product:
				maxprod = product
	return maxprod


def diag_2(grid, cycle=4):
	# Returns the largest product of 4 numbers from upper left to lower right
	maxprod = 1
	numcol = len(grid[0])
	numrow = len(grid) - 1

	for i in range(numrow - cycle):
		for j in range(numcol - cycle):
			product = 1
			for p in range(cycle):
				product *= grid[i + p][j + p]
			if maxprod < product:
				maxprod = product
	return maxprod


# TODO: write code to run all these methods and return the largest value
def run_all(grid):
	maxprod = [row_test(grid), column_test(grid), diag_1(grid), diag_2(grid)]
	return max(maxprod)


# ======= Use our functions to find the result! ======= #

grid = make_grid_from_file("euler_11_input.txt")
maxprod = run_all(grid)

print("\nThe answer to Euler #11 is:", maxprod)
