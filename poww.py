n = int(input())
sum = 0
#res = pow(n, 2)
#print(res)

for i in range(2, n+1, 2):
    re = pow(i, 2)
    print("re", re)
    print(i)
    sum = sum + re
    print("sum", sum)
