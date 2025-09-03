n = input().split()
num_list = [ ]
tower_list  = [ ]
max_seen = 0

for i in n:
    num_list.append(int(i))
print(num_list)

for tower in num_list:
    if tower > max_seen:
        tower_list.append(tower)
        max_seen = tower
print(tower_list)
