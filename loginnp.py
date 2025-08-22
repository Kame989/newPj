'''u = input("name : ").strip()
p = input("password : ").strip()

ur_u = input("name(login) : ").strip()
ur_p = input("password(login) : ").strip()

if u == ur_u and p == ur_p:
    print("Success")
else:
    print("Error")
'''

u = input().split(":")[1].strip()
p = input().split(":")[1].strip()

ur_u = input().split(":")[1].strip()
ur_p = input().split(":")[1].strip()
'''
if u == ur_u and p == ur_p:
    print("Success")
else:
    print("Error")'''

print(u, p, ur_u, ur_p)  # Debugging output to check values