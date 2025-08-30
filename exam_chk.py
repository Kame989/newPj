stu = input().strip().split("-")
ans = input().strip().split("-")

stu_list = []
ans_list = []

for ch in stu:
    stu_list.append(ch)
print(stu_list)    

for ch in ans:
    ans_list.append(ch)
print(ans_list)

sc = 0
if len(stu_list) != len(ans_list):
    print("Error")
else:
    for ch in range(len(stu_list)):
       if stu_list[ch] == ans_list[ch]:
           sc = sc + 1
    
    print(f'Total score = {sc}/{len(stu_list)}')