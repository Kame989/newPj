n = input("")

rev = n[::-1]
rem_0 =rev[1:] #starts the slice from index 1 (the second character) and goes to the end of the string.
print(f"{n}{rev}")
print(f"{n}{rem_0}")

'''
print(n.split(",")) #split text show as list using  , as indicator to split
print(n.upper())
print(n.lower())
print(n.strip()) #remove white space
print(n[:3]) #slicing from 0 - 3
print(n[2:]) #slicing from 2(not include 2) -the end
print(n[-4:-2]) #slicing start fromthe back last char or 1st  from back = -1, 2nd =-2, so -4th index = h, -2nd index= j but in python end that n-1 ,so = till-3rd index = a
print(len(n))

for i in (n):
    print(i)

'''