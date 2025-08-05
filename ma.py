import numpy as np

r = int(input())
c = int(input())
matrix = [ ]


for i in range (r):
    m_list = [ ]
    for j in range(c):
        el = float(input(f"element {i+1}, {j+1}: "))
        m_list.append(el)
    matrix.append(m_list)

'''
for m_r in matrix:
    print(m_r)

min_v = matrix [0] [0]

for row in matrix:
    for val in row:
        if val < min_v:
            min_v =val

print(min_v)

max_v = matrix[0 [0]]
for row in matrix:
    for val in row:
        if val > max_v:
            max_v = val

print(max_v)
'''
#find max min
arr = np.array(matrix) #convert matrix  to ndarray
min_v = np.min(arr) #find min in array
max_v =np.max(arr) #find max in array

print(max_v)

#scale to[0,1]
denom = max_v - min_v

for row in matrix:             # ✅ this loops each row
    scaled_row = []
    for x in row:
        if denom == 0:
            scaled = 0.0
        else:
            scaled = (x - min_v) / denom
        scaled_row.append(f"{scaled:.4f}")
    print(" ".join(scaled_row))



'''
for i in range (r):
    for j in range (c):
        print(matrix[i][j], end=" ")
    print()
'''
