n = 3
m_list = [ ]
for i in range(n):
    m = int(input())
    m_list.append(m)
print(m_list)


v1 = m_list[0]
v2 = m_list[1]
v3 = m_list[2]

sum = v1+v2
if v3 > sum:
    print("C is BIG")
else:
    print("a+b>c")
