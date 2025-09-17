ba = 0

while True:
    com = input().strip()
    if com == "exit":
        break
    
    parts = com.split()
    action = parts[0]
    x = float(parts[1])

    if action == "deposit":
        ba = ba+x
    elif action =="withdraw":
        if x > ba:
            break
        else:
            ba = ba-x

print(f"balance = {ba:.2f}")

