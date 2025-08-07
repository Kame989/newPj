n = int(input())
n_list = [ ]

for element in range(n):
    num = int(input())
    n_list.append(num)

print(n_list)

#re = n_list[ : :-1 ]
#print(re)

for i in range (len(n_list)):
    re = n_list[ : :-1 ]
print(*re, sep='\n')
