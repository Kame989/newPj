n = input().strip()
m = n.split(",")

ok = True
if not(1 <= len(m[0]) <= 3 and m[0].isdigit()):
    ok = False

for unit in m[1:]:
    if not (len(unit) ==3 and unit.isdigit()):
        ok = False
        break

if ok:
    print("Correct")
else:
    print("Incorrect")




