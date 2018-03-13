# -*- coding: utf-8 -*-
"""
Euler #17
Number Letter Counts

Created on Sun Mar 11 2018

@author: Maxwell
"""

# Grab all the strings we will use
ones = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

# Grab the length of the strings used
ones = [len(i) for i in ones]
teens = [len(i) for i in teens]
tens = [len(i) for i in tens]
hndrd = len("hundred")
b_and = len("and")

# Count the numbers below 100
c_1_9 = sum(ones)  # sum of 1 - 9
c_10_19 = sum(teens)  # sum of 10 - 19
c_20_99 = 10 * sum(tens) + 8 * c_1_9
c_1_99 = c_1_9 + c_10_19 + c_20_99

# Count the rest of the numbers excluding multiples of 100
c_100_999 = 100 * c_1_9 + 9 * c_1_99 + 9 * hndrd + 891 * (hndrd + b_and)

# Add in the first 99 and all the hundreds
result = c_1_99 + c_100_999 + len("one") + len("thousand")

print(result)
