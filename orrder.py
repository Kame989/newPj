n = int(input())
m_list = [ ]

for element in range(n):
    num = int(input())
    m_list.append(num)
print(m_list)

for i in range(len(m_list)):
    m_list[i] = int(m_list[i])
    m_list.sort(reverse=True)
    
print(*m_list, sep= '\n')