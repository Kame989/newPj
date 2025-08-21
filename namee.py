n =int(input())
name_list = [ ]
for i in range(n):
  name = input()
  name_list.append(name)
  
if n == 1:
  print(name_list[0])
  #  # แค่ 2 คน → คั่นด้วย and
elif n == 2:
  print(name_list[0] + " and " + name_list[1])
else:    # มากกว่า 2 คน → คนก่อนหน้าคั่นด้วย , คนสุดท้ายคั่นด้วย and
  print(", ".join(name_list[:-1])+ " and " + name_list[-1])