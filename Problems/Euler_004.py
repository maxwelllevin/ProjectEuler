# -*- coding: utf-8 -*-
"""
Euler #4
Largest Palindrome Product of Two Three-Digit Numbers

Created on Mon Sep  4 20:32:47 2017

@author: Maxwell
"""


def is_palindrome(number=-1):
    """ Converts an integer input into a string, then checks that
        string for symmetry. Returns True if number is palindromic, 
        False otherwise """
    string_num = str(number)
    string_len = len(string_num)
    string_end = string_len - 1
    
    for index in range(string_len):
        pal_index = string_end - index
        if string_num[index] != string_num[pal_index]:
            return False    
    return True


def test_products_of_three_digits(NUM1 = 900, NUM2 = 900):
    
    large_pal = 9009 #91 x 99
    for num1 in range(NUM1,1000):
        for num2 in range(NUM2, 1000):
            number = num1 * num2
            if number > large_pal and is_palindrome(number):
                large_pal = number
    return large_pal


large_pal = test_products_of_three_digits()
print ("The Largest Palindrome Product of Two Three-Digit numbers is", large_pal)