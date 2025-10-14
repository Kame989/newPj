n = input().replace(',', ' ').split()
s = int(input())
sum = 0
m_list = [ ]

for i in n:
    m_list.append(int(i))

print(m_list)

for i in range(len(m_list)):
    for j in range(i+1, len(m_list)):
        if m_list[i] + m_list[j] == s:
            print(i,j) # แสดง index ของคู่ที่บวกกันได้ s
        else:
            print("0")

