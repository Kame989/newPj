n = int(input("Number: "))
my_list  = [ ]

for i in range (n):
    item = int(input())
    my_list.append(item)
    my_list.sort()
    print(f"ROW {i+1} : {my_list}") 