my_list = []

while True:
    x = input()
    if x == "0":
        break
    my_list.append(int(x))
  
order = input("min or max: ").lower()

if order == "min":
    my_list.sort()
    print(*my_list)
elif order == "max":
    my_list.sort(reverse=True)
    print(*my_list)
else:
    print("error")
