n = input().strip().lower()
count = { } #ใช้ {} (dict) → เหมาะกับการนับจำนวนแต่ละ ตัวอักษร โดยตรง
m_list = list(n)
print(m_list)

#หมายถึง ตรวจสอบว่าตัวอักษรนี้เคยนับมาแล้วหรือยัง
#ถ้า เคยเจอแล้ว → ก็เพิ่มจำนวนครั้งที่เจอขึ้นอีก 1
for ch in n:
    if ch in count:
        count[ch] = count[ch] + 1 #ch more than 1
    else:
        count[ch] = 1 #ch only 1

re = ' '
for ch in n:
    if count[ch] == 1 :
        re = re + '('
    else:
        re = re + ')'

print(re)
    