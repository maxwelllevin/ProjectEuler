# -*- coding: utf-8 -*-
"""
Euler #15
Lattice Paths

Created on Sun Mar 11 2018

@author: Maxwell
"""

"""This problem asks the number of paths there are from the top left corner of a 20x20 grid to the bottom right 
corner of the grid if one can only make the turns down or right. Since the total number of right turns must be 20 and 
the total number of down turns must also be 20, this turns into a permutation problem. We simply seek the number of 
permutations of 20R and 20D. That is, nCr(20+20, 20). """

import scipy.special as sp

print(sp.comb(20 + 20, 20))
