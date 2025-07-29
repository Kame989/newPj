import math

n = int(input())
sq_root = math.sqrt(n)

if sq_root.is_integer():
    print(f"{n} is a int")
else:
    print(f"{n} is float")

'''The .is_integer() method in Python is a built-in method specifically for float objects. 
It determines whether a float value can be represented as an integer without any loss of precision. 
Functionality:
It returns True if the float has no fractional part after the decimal point (e.g., 5.0, -2.0).
It returns False if the float has a non-zero fractional part (e.g., 3.14, 7.5).
'''
# Returns True because 5.0 is an integral value
print((5.0).is_integer())

# Returns False because 3.14 has a fractional part
print((3.14).is_integer())

# Returns True for negative integral floats
print((-2.0).is_integer())

# Attempting to use on an integer directly raises an AttributeError
# print((5).is_integer()) # This will cause an error