n = input().split("+")
m_list = [ ]
for num in n:
    m_list.append(int(num))

print(m_list)
m_list.sort()
print(m_list)


for i in range(len(m_list)-1):
    print(m_list[i], end="+")
print(m_list[-1])

