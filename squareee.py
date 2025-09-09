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



for i in range(n):
  print(" " * (n-i-1) + "*" * (n+1))