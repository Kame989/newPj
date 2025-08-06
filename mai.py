name_d = ["Name", "Address", "Gender", "Tel"]
m_list = [ ]

for item in name_d:
    detail = input(f"enter {item} : ")
    m_list.append(detail)
    print(f"{item} : {detail}")
'''
for i in range(len(name_d)):
    print(f"{name_d[i]} : {m_list[i]}")
'''
i = 0
for item in name_d:
    print(item, ":", m_list[i])
    i +=1