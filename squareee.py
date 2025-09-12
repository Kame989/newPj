n= int(input())
'''
n = int(input())

for i in range(n):
    for j in range(n - 1, i, -1):  # ช่องว่าง: (n-1) - i
        print(" ", end = "")
    for k in range(0, i + 1, 1):   # * ซีกซ้าย: i + 1
        print("*", end = "")
    for l in range(n, i, -1):      # * ซีกขวา: n - i
        print("*", end = "")
    print()
    

OR
    '''



for i in range(0,n,1):
  print("-" * (n-i-1) + "*" * (n+1))
#Because each print() automatically adds a newline (\n) at the end
'''print("123")
print("456")
Output:

Copy code
123
456
Because each print() automatically adds a newline (\n) at the end.

⚡ If you want them on the same line, you override with end="":

python
Copy code
print("123", end="")
print("456")
Output:

Copy code
123456
So rule of thumb:

print() = adds a newline by default

print(..., end="") = no newline'''