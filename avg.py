n = int(input())
m_list = [ ]

for i in range (n):
    num = int(input())
    m_list.append(num)

print(m_list)
print(type(m_list[0]))

total = sum(m_list)
print(total)
avg = total/len(m_list)
print(avg)