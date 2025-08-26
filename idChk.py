id = input()

m_list = [ ]

for i in id:
    m_list.append(int(i))

print(*m_list)

total = 0

for i in range(12): # 0-11
    w = 13 - i # i แรก = 0, so 13-0 = 13
    total = total + (m_list[i]*w)
print(total)

chk_digit = (11-(total%11))%10
if chk_digit == m_list[12]:
    print("Pass")
else:
    print("Fail")