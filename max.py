# Get user input and split it into a list
'''user_input = input("Enter elements separated by space: ").split()

print("List:", user_input)
for item in user_input:
    print(item)
'''
my_list = [ ]
while True:
    user_input = int(input("Enter num: "))
    if user_input == 0:
        break
    else:
        my_list.append(int(user_input))

if  my_list:
    ch = input("enter min or max: ").lower()
    if ch == "min":
        my_list.sort()
        print(my_list)
        for item in my_list:
            print(item)
    elif ch == "max":
        my_list.sort(reverse=True)
        print(max(my_list))
        print(my_list)
        for item in my_list:
            print(item)
    else: 
        print("error")
