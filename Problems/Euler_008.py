# -*- coding: utf-8 -*-
"""
Euler #8 
Greatest product of 13 adjacent digits in a thousand-digit number

Created on Tue Sep  5 20:18:01 2017

@author: Maxwell
"""



def find_product_of_digits(string):
    """ Returns the product of all the digits in a string"""
    # Variable to store our product
    product = 1
    
    # Iterate through our string
    for index in range(len(string)):
        product *= int(string[index])
    
    # Return the product
    return product



def find_largest_consecutive_product(consecutive_digits=1, string=''):
    """ Returns the largest product of a specified number of consecutive digits
        within a given string"""
    # Create a variable to store our product and a list to send to find_product_of_digits
    product = 1
    subset_string = []
    product_string = []
    
    # Loop through our string to test all the substrings
    for index in range(len(string) - consecutive_digits + 1):
        subset_string.clear()
        for i in range(consecutive_digits):
            subset_string.append(int(string[index + i]))
        test_product = find_product_of_digits(subset_string)
        if test_product > product:
            product = test_product
            product_string = subset_string
            #print(product_string)
    
    # Return the largest product and print the associated string
   # print(product_string)
    return product



# ======= Test 'find_product_of_digits' ======= #

#test_string = '146' # Product should be 24
#print(find_product_of_digits(test_string))




# ======= Test 'find_largest_consecutive_product' ======= #

test_string = '7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450'
print(find_largest_consecutive_product(13, test_string))


