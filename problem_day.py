data = input().split()
m_list = [ ]

for i in range(len(data)):
    m_list.append(int(data[i]))
    
n = int(data[0])
m =int( data[1])
k = int(data[2])
a = int(data[3])
   
#print(*m_list)

d = m - n +1
print(d)

s = d/2 *(2*k +(d-1)*a)
dif = 1234 -s

if s >= 1234:
    print("YES")
else:
    print(int(dif))


