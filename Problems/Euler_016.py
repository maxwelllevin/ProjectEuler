# -*- coding: utf-8 -*-
"""
Euler #15
Power Digit Sum

Created on Sun Mar 11 2018

@author: Maxwell
"""

# Can actually just do this in python
number = 2**1000

# Add all of its digits
num = str(number)
sum = sum([int(i) for i in num])
print(sum)
