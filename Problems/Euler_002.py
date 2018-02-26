# -*- coding: utf-8 -*-
"""
Euler #2

Created on Thu Aug 31 17:30:51 2017

@author: Maxwell
"""

from functools import lru_cache

@lru_cache(maxsize = 1000000)
def fibonacci(n):
    """Returns the Nth fibonacci number"""
    if n == 1:
        return 1
    if n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)


def add_fibonacci(limit = 1):
    """Returns the sum of fibonacci numbers under 'limit' """
    add_fib = 0
    n = fibonacci(1)
    i = 2
    while n < limit:
        if n%2 == 0:
            add_fib += n
            print(n)
        n = fibonacci(i)
        i += 1
    print ("Considered", i, "fibonacci numbers under", limit)
    return add_fib

n = add_fibonacci(4000000)
print("The sum of even fibonacci numbers under 4 million is:", n)