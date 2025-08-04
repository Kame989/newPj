m = int(input())
sum = 0

for i in range(1,13):
    print(f"{m} x {i} ={m*i}")
    sum =sum+(m*i)

sum = float(sum)    
format_sum = "{:,}".format(sum)
print(f"sum : {format_sum}")