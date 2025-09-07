my_list =  [ ]

while True:
    item = input()
    if item == "exit":
        if not my_list:
            print("Shopping list")
            print("Nothing...")
        else:
            item_counts = { } #dictionary
            for ch in my_list:
                if ch in item_counts:
                    item_counts[ch] = item_counts[ch]+1
                else:
                    item_counts[ch] = 1

            print("Shopping list")
            for key in item_counts:
                print(f'Buy {item_counts[key]} {key}')
        break
    else:
        my_list.append(item)
