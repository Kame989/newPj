line = input()
parts = line.split()

A, B, C = [ ], [ ], [ ]
cur = None #or use[ ]

for word in parts:
    if word == "A:" :
        cur = A
    elif word =="B:" :
        cur = B
    elif word == "C:" :
        cur = C
    else:
        cur.append(word)

# ใช้ set นับชนิดไม่ซ้ำ
a_count = len(set(A))
b_count = len(set(B))
c_count = len(set(C))

if a_count >= b_count and a_count >= c_count:
    print("A")
elif b_count >= a_count and b_count >= c_count:
    print("B")
else:
    print("C")