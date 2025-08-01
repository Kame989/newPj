# Prompt the user for input and store the numbers
num1, num2 = map(int, input("Enter two numbers separated by a space: ").split())

# You can now use num1 and num2 as integers
print(f"The first number is: {num1}")
print(f"The second number is: {num2}")
print(f"Their sum is: {num1 + num2}")

count = 0

for num in range(num1, num2 +1):
    count += str(num).count('9')

print(count)
'''# 1. อ่านค่าตัวเลข 2 ตัวจากผู้ใช้ (สมมติว่า start ≤ end เสมอ)
start = int(input())   # เช่น กรอก 80
end   = int(input())   # เช่น กรอก 100

# 2. ตัวแปรเก็บผลลัพธ์ (จำนวนครั้งที่พบ '9')
count_9 = 0

# 3. ตรวจทุกตัวเลขในช่วง [start, end]
for num in range(start, end + 1):
    # แปลงเป็นสตริง แล้วนับว่าในตัวเลขนี้มี '9' กี่ตัว
    count_9 += str(num).count('9')

# 4. พิมพ์ผลลัพธ์ออกมา
print(count_9)

'''