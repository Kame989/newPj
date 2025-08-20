n1 = input().split()
#list1 = [int(i) for i in n1]
list1 = [ ]
for i in n1:
    list1.append(int(i))

n2 = input().split()
#list2 = [int(i) for i in n2]
list2 = [ ]
for i in n2:
    list2.append(int(i))

# 1) ถ้า list ยาวไม่เท่ากัน → Invalid
if len(list1) != len(list2):
    print("Invalid")
else:
    sum_list = [ ]
    invalid = False

    # 2) บวกค่าทีละตัว
    for i in range(len(list1)):
        total = list1[i] + list2[i]
        if total >= 32548:
            invalid = True
        sum_list.append(total)

    # 3) ตรวจว่ามี Invalid หรือไม่
    if invalid:
        print("Invalid")
    else:
        print(*sum_list)
