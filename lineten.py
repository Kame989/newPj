n = int(input())
count = 0
for i in range (2, n+1, 2):
    print( i, end = " ")
    count = count + 1
    if count%10 == 0:
        print( )