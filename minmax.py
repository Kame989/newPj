n = int(input())
m_list = [ ]


for x in input().split():
    m_list.append(int(x))

print(m_list)

max_v = max(m_list)
min_v = min(m_list)
print(max_v, min_v)
