# -*- coding: utf-8 -*-
"""
Euler #10
Summation of Primes below 2 million

Created on Thu Sep  7 13:46:33 2017

@author: Maxwell
"""

def import_data_from_file(filename):
    """ Opens a given file and copies all information into a list"""
    # Create our list
    data = []
    
    # Open the file and read info into data[]
    file = open(filename, 'r')
    for line in file:
        data.append(int(line))
    
    # Close the file
    file.close()
    
    # Return the data list
    return data



def add_list_elements(add_list, limit=2000000):
    """ Returns the sum of all elements in the list whose values are less than the limit"""
    # Create a variable to store the sum
    sum = 0
    
    # Iterate through the list
    for element in add_list:
        if element < limit:
            sum += element
    
    # Return the sum
    return sum



# ====== Solve Euler #10 ====== #


# Import datetime module to calculate program run-time
import datetime
before = datetime.datetime.today()


# Import primes from a text file output from our Sieve of Atkin program
file = 'primes_under_two_million.txt'
primes = import_data_from_file(file)

# Add up all the primes below two million and print the result
sum_of_primes = add_list_elements(primes)
print("The sum of all primes below two million is:", sum_of_primes)

# Calculate and print the time taken to run this program
after = datetime.datetime.today()
print("Program ran for:", after-before)

