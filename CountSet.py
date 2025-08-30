'''
m_set = set(input().split())
print(*m_set)
print(len(m_set))
'''
n = input().split()
m_list = [ ]

for ch in n:
    num = int(ch)
    if num == 0:
        break
    m_list.append(num)

m_set = set(m_list)
print(len(m_set))
