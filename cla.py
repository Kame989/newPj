x = int(input())
n = int(input())
m_list = [ ]

for i in range(n):
    con = input().split()
    f = int(con[0])
    t = int(con[1])
    name = con[2]
    

    if f <= x <= t:
        m_list.append(name)
    
'''
เงื่อนไข if f <= x <= t: หมายถึง

ถ้า x อยู่ในช่วง f ถึง t → เก็บชื่อหมวดหมู่ไว้ (append)

ถ้า x ไม่อยู่ในช่วง f ถึง t → จะไม่ทำอะไรเลย (ข้ามไปยังรอบถัดไปของลูป)
x = 4
f = -3
t = 3
ตรวจสอบ if -3 <= 4 <= 3: → False → ไม่ทำอะไร

python
Copy
Edit
x = 4
f = 4
t = 4
ตรวจสอบ if 4 <= 4 <= 4: → True → เก็บชื่อหมวดหมู่

'''
# แสดงผลหมวดหมู่ทั้งหมดที่ตรง
for element in m_list:
    #print(element)
    if m_list:              # ถ้ามีอย่างน้อย 1 หมวดหมู่
        print(m_list[0])    # แสดงเฉพาะตัวแรก
