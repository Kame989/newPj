n = input()
len_n = len(n)

for i in range(0,len_n,1):
    for j in range(0,len_n-i-1,1):
        print(" ", end = " ")
    for k in range(i,0,-1):
        print(n[k], end = " ")
    print(n[0], end = " ")
    for k in range(1,i+1,1):
        print(n[k], end = " ")
    print()