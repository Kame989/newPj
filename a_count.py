n = input().split()
m_list = [ ]

for ch in n:
    m_list.append(ch.lower())

print(m_list)

count = 0
for word in m_list:
    for char in word:
        if char == 'a':
            count += 1

print(count)