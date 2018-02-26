# -*- coding: utf-8 -*-
"""
Euler #5
Smallest multiple of all numbers from 1 to 20

Created on Mon Sep  4 21:01:54 2017

@author: Maxwell
"""


def factor_to_prime(number):
    """Returns a list containing the prime factorization of 'number' """
    # Create an empty list to contain the prime factorization
    prime_factors = []
    
    # Start division at the first prime number and store all prime factors
    divisor = 2
    while divisor != number:
        if number % divisor == 0:
            number /= divisor
            prime_factors.append(divisor)
        else:
            divisor += 1
    
    # After division, the largest prime factor is what remains of 'number'
    # Store 'number' in the list and return the list
    prime_factors.append(int(number))
    return prime_factors



def combine_lists(a_list=[], b_list=[]):
    """Returns a combination of two lists. Somewhat like a union, but for lists.
        Also preserves the larger amount of copies of an item between 2 lists."""
    # Copy a_list to new_list
    new_list = a_list
    
    # If b_list has more copies of a specific item, copy excess to new_list
    for item in a_list:
        if b_list.count(item) > a_list.count(item):
            num_copy = b_list.count(item) - a_list.count(item)
            for copiesleft in range(num_copy):
                new_list.append(item)
    
    # Copy the remaining elements of b_list to new_list
    for item in b_list:
        if a_list.count(item) == 0:
            num_copy = b_list.count(item)
            for copiesleft in range(num_copy):
                new_list.append(item)
    
    # Sort the list and then return it
    new_list.sort()
    return new_list
    

def lcm_integers_under(limit = 2):
    """ Creates a list containing the prime factors of the lcm of all
        positive integers under the given limit """
    # Create two lists: 'factored' stores prime factors for a given integer,
    # and 'lcm' stores an accumulation of prime factors over the range 2->limit
    lcm_factors = []
    factored_int = []
    
    # Calculate prime factorizations and let them accumulate in 'lcm'
    for integers in range(2, limit):
        factored_int = factor_to_prime(integers)
        lcm_factors = combine_lists(lcm_factors, factored_int)
        factored_int.clear()
        
    # Sort and return the accumulated list of factors
    lcm_factors.sort()
    return lcm_factors



def mult_through_list(mult_list):
    """ Returns the product of all the elements of a given list """
    # Create 'product' to store the product of all the elements
    product = 1
    
    # Iterate through, multiplying product by each item
    for item in mult_list:
        product *= item
    
    # Return the product
    return product
    

# ======== Test out factor_to_prime ========= #

#print(factor_to_prime(98))



# ======== Test out combine_lists ======== #

#list1 = factor_to_prime(6)
#list2 = factor_to_prime(8)
#print(combine_lists(list1, list2))


# ======== Test out lcm_integers_under && mult_through_list =========#
import datetime

before = datetime.datetime.today()

lcm_list = lcm_integers_under(100)
print(lcm_list)


product = mult_through_list(lcm_list)
print(product)

after = datetime.datetime.today()
print(after-before)
