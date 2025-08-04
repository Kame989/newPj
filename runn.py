r =int(input("round: "))
m = int(input("money: "))
t = r*m
for i in range (r):
    print(f"{i+1}-{m}")
print(t)