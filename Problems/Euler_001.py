# -*- coding: utf-8 -*-
"""
Euler #1

Created on Thu Aug 31 16:19:50 2017

@author: Maxwell
"""

multiples = []

def find_sum_of_multiples(num1, num2, limit):
    """Returns the sum of multiples of two numbers under a given limit """
    sum = 0
    for i in range(1, limit):
        if i%num1 == 0 or i%num2 == 0:
            sum += i
            multiples.append(i)
    return sum
    
print (find_sum_of_multiples(3,5,1000))
#print(multiples)

def find_sum_of_list(some_list):
    sum = 0
    for item in some_list:
        sum += item
    return sum

print(find_sum_of_list(multiples))