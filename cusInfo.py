n = int(input())
c_list = [ ]
curr_year = 2017

for element in range(n):
    f_name = input().strip()
    year = int(input().strip())
    sex = input().strip()

    age = curr_year - year

    c_list.append({
        "name" : f_name,
        "age" : age,
        "gender" : sex
    })

print("--Customers Information--")
for cust in c_list:
    print(f"{cust['name']} (age : {cust['age']})")
    
