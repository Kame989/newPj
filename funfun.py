def mfun(x):
    return x+1
mfun(2)

y = mfun(3)
print(y)

#ถ้าไม่ return จะได้ค่า None
def mfun1(x):
    x+1
h = mfun1(3)
print(h)

def mfun3(x,y):
    return x+y
z = mfun3(2,3)
print(z)

#ฟังก์ชันที่มี return หลายค่า
def mfun4(x,y):
    return x+y, x-y
z, w = mfun4(2,3)
print(z, w)

#ฟังก์ชันที่มี return หลายค่า แต่รับค่ากลับแค่ตัวเดียว จะได้ค่าเป็น tuple
def mfun5(x,y):
    return x+y, x-y
z  = mfun5(2,3)
print(z)

#ฟังก์ชันที่มีจำนวนอาร์กิวเมนต์ไม่จำกัด สนใจลำดับ
def msum(*x):
    return sum(x)
s = msum(1,2,3,4,5)
print(s)

#ฟังก์ชันที่มีจำนวนอาร์กิวเมนต์ไม่จำกัด สนใจชื่อ or keyword
def rec_a(**x):
    return x['w']*x['h']
a = rec_a(w=2, h=3)
print(a)

import math
print(math.sin(math.pi/4))
print(math.cos(math.pi/4))
print(math.tan(math.pi/4))
trigon = [math.sin, math.cos, math.tan, math.sinh, math.cosh, math.tanh]
for f in trigon:
    print(f(math.pi/4))
#or 
print([f(math.pi/4) for f in trigon])

