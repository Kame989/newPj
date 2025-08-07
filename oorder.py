m_list = [ ]

#use for loop to collect input(type =int) 
for element in range (5):
    n = int(input())
    m_list.append(n) #adding n into list 5 times
    print(m_list)

#using for loop to convert each string to int by using int()
for i in range(len(m_list)): 
    m_list[i] = int(m_list[i])
    m_list.sort()
print(*m_list, sep='\n')

'''
m_list.sort() #sorting m_list
print(m_list)
print(*m_list) #Using the * operator (unpacking)'''




'''
decending
m_list = [ ]
for item in range(5):
  n = int(input())
  m_list.append(n)

#print(m_list)

for i in range(len(m_list)):
  m_list[i] =int(m_list[i])
  m_list.sort(reverse=True)
print(*m_list, sep='\n')
'''