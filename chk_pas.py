n = input().split(",")
names = ["Man", "Non", "Miv"]

m_list = [ ]

for word in n:
    m_list.append(word)

winner = None

for i in range(len(m_list)):
    pw = m_list[i].strip()
    name = names[i]

    if not (6 <= len(pw) <=12):
        continue

    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False
    allowed_special = set("$#@")
    ok = True

    for ch in pw:
        if ch.islower():
            has_lower = True
        elif ch.isupper():
            has_upper = True
        elif ch.isdigit():
            has_digit = True
        elif ch in allowed_special:
            has_special = True
        else:
            ok = False
            break

    if ok and has_lower and has_upper and has_digit and has_special:
        winner = pw +" ("+ name + ")"
        break

if winner:
    print(winner)
else:
    print("Error")
