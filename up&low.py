n = input().lower()

m_list = [ ]

for i in range(len(n)):
    if i % 2 == 0:
         ch = n[i].lower()  
    else:
         ch = n[i].upper()
    m_list.append(ch)

print("".join(m_list))