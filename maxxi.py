n_list = [ ]

for i in range (3):
    num = int(input("num: "))
    n_list.append(num)
    #print(f"{i} : {num}")

max_v =max(n_list)
print(f"MAX : {max_v}")