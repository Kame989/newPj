# อ่าน n (เราอาจไม่ต้องใช้ตัวแปรนี้ต่อถ้าอ่าน list ได้ตรงๆ)
n = int(input())

# อ่าน list ของตัวเลข
data = list(map(int, input().split()))
'''
if you type 4 2 5 7 1, Python sees it as the string "4 2 5 7 1".
parts = line.split()
# parts is now ["4", "2", "5", "7", "1"]
By default, .split() looks for spaces and cuts the string at each space.

map() is like for loop but it more shorter

parts = input().split()
data = []
for x in parts:
    data.append(int(x))

same as

data = list(map(int, input().split()))

'''


# อ่านตัวเลขที่ต้องการค้นหา
x = int(input())

# เช็กว่า x อยู่ใน data หรือไม่
if x in data:
    print("Yes")
else:
    print("No")
