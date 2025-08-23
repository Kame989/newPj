'''stu = list(map(int, input().split()))
print(stu)

or
'''
stu = [ ]
for  x in input().split():
    stu.append(int(x))
print(stu)

tch = [ ]
for x in input().split():
    tch.append(int(x))
print(tch)


sc= 0

for i in range(len(stu)): #วนเท่ากับจำนวนข้อ
    if stu[i] == tch[i]: #บวกคะแนน
        sc =sc+1

print(sc)