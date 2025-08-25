n = int(input())
m_list = [ ]


for ch in range(n):
    m = int(input())
    m_list.append(m)
print(m_list)

total =sum(m_list)

'''or
for i in range(len(m_list)):
    print(total -m_list[i])
'''
for i in range(len(m_list)):
        total = total - m_list[i]
        print(total)
        total = sum(m_list)

