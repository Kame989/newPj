import math

a = int(input())
b = int(input())

a = a**2 #pow(a, 2)
b = b**2 #pow(b, 2)
re = math.sqrt(a+b)
print(a+b)
print(int(re))

'''
or
A = a*a
B = b*b
C = A + B
c = int(C**0.5)
print(C)
print(c)
'''
