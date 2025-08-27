n = input()
words = n.split(".")
print(words)

n_int = [ ]

if len(words) != 4:
    print("No")
else:
    valid = True
    for ch in words:
        if not ch.isdigit():
            valid = False
            break
        if int(ch) > 255:
            valid = False
            break
        n_int.append(int(ch))

if valid:
    print("Yes")
else:
    print("No")
'''1 line print
print("yes" if valid else "no")
'''


