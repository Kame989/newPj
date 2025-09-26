import math

# รับค่า n และ x
n_x = input().split()
n = int(n_x[0])
x = int(n_x[1])

# รับราคาปากกาเป็นสตริง
prices_str = input().split()

total = 0
for i in range(n):
    p = int(prices_str[i])            # แปลงเป็นตัวเลขทีละตัว
    add = math.ceil(p * x / 100)      # คำนวณส่วนเพิ่มและปัดขึ้น
    total += p + add                  # บวกเข้า total

print(total)