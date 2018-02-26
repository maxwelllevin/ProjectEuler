# -*- coding: utf-8 -*-
"""
Euler #6
Difference between sum of squares and square of sums of first 100 natural numbers

Created on Tue Sep  5 19:07:49 2017

@author: Maxwell
"""


def sum_of_squares(limit):
    """Returns the sum of the squares of the naturals from 1 to 'limit'
        Ex: limit = 3
            1*1 + 2*2 + 3*3 = 14 """
    # Create variable to store the sum
    sum = 0
    
    # Iterate through naturals within our specified range
    for number in range (1, limit + 1):
        sum += number ** 2
    
    # Return the sum
    return sum



def square_of_sums(limit):
    """Returns the square of the sums of the naturals from 1 to 'limit'
        Ex: limit = 3
            (1 + 2 + 3)^2 = 36 """
    # Create a variable to store the sum
    sum = 0
    
    # Iterate through the naturals within our specified range
    for number in range(1, limit + 1):
        sum += number
    
    # Return the square of the sum
    return sum ** 2



# ======= Test our functions with 'limit = 100' ======= #

limit = 100

sum_squares = sum_of_squares(limit)
square_sums = square_of_sums(limit)

print("The sum of squares =", sum_squares)
print("The square of sums =", square_sums)
print("The difference between the two is:", square_sums - sum_squares)

