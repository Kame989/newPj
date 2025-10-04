#User function Template for python3

#Write the complete argumentFunction below.
#The function should take two arguments a and b
#The function should return a+b
#code here

#Write the argumentFunction above.
def  argumentFunction(a,b):
    return a+b

print(argumentFunction(2,3))

# Using String Conversion (Simplest for any number, including negative):
def first_digit(n):
    n_str = str(n)
    if n_str[0] =='-':
        return int(n_str[1])
    else:
        return int(n_str[0])
    
print(first_digit(12345))

# Using Mathematical Operations (Without string conversion):
def first_digit_math(n):
    if n == 0:
        return 0
    n = abs(n)  # Handle negative numbers
    while n >=10:
        n //= 10
    return n

print(first_digit_math(6789))

import math

def first_digit_log(n):
    if n == 0:
        return 0
    n = abs(n)  # Handle negative numbers
    if n < 1: # Handle numbers between 0 and 1
        return int(str(n)[2]) # First digit after decimal eg 0.1
    
    power_of_ten = int(math.log10(n))    # power_of_ten of 6789 = 3 ,power_of_ten of 4567 = 3
    first_digit = n // (10**power_of_ten) # 6789 // 1000 = 6, 4567 // 1000 = 4
    return int(first_digit)

    
print(first_digit_log(0.1567))
print(first_digit_log(4567))

#print(power_of_ten)  # 3
#print(first_digit)   # 6