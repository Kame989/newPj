import numpy as np
r  = int(input("enter row: "))
c = int(input("enter column: "))

matrix = [ ]

print("enter num: ")


for i in range (r):
    m_list= [ ]
    for j in range(c):
        m_list.append(int(input())) #user input each number
        
    matrix.append(m_list) #adding row to matrix



print("ur {r} * {c} matrix is: ")
print(matrix)


'''
for i in range(r):
    for j in range(c):
        print((matrix[i][j] -min_val)/max_val-min_val, end=" ")
    print()

'''