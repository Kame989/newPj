n = input()
m = n.split()
m_list = [ ]

for ch in m:
    m_list.append(ch)
#print(" ".join(m_list))

m_list.reverse()
print(" ".join(m_list))

