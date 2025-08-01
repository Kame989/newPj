# 1. Read the whole line, replace "==" with a space, then split into two pieces
data = input("Enter two numbers (e.g. 45==74 or 45 74): ").replace("==", " ")
n1, n2 = map(int, data.split())

'''
or n1, n2 = [int(x) for x in input("enter two numbers: (e.g. 45==74)").split()]
map()= map(function, iterable) applies the function to each item in the iterable
or 
def make_even(num):
    if num % 2 == 1:
        return num + 1
    else:
        return num

x = [1, 2, 3, 4]
y = [ ]
for num in x:
    y.append(make_even(num))

print(list(y))

data = "1 2 3 4".split()      # ["1","2","3","4"]
numbers = list(map(int, data))  # [1, 2, 3, 4]
print(numbers)

'''

# 2. Print the bigger one
print(max(n1, n2))
