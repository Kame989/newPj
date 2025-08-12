n = int(input())
m_list = [ ]

for item in range (n):
    prod = int(input())
    m_list.append(prod)

print(m_list)

target = int(input())

position =[ ]
for i in range (len(m_list)):
    if m_list [i] == target:
        position.append(i+1)

print(type(position[0]))  # int or str

if position:
    s ='' 
    for i in range(len(position)):
        if i > 0:
            s = s+ ","
        s = s + str(position[i])
    print("Position: " + s)
else:
    print("Not Found")