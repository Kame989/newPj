n = int(input().strip())

width = 2 * n + 1  # ความกว้างรวมของต้น

# พุ่มซ้อนทีละชั้น
for tier in range(1, n + 1):
    for r in range(1, tier + 2):  # ความสูงของพุ่มชั้นนี้ = tier + 1
        stars = 2 * r - 1
        print(("*" * stars).center(width))#.center(width) = “จัดให้อยู่ตรงกลางโดยเติมตัวอักษรให้ได้ความกว้างตาม width”

# ลำต้นและฐาน
print(" " * n + "|")
print("=" * n + "V" + "=" * n)