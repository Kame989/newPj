name = input( ).strip( )
words = name.split( )
result = [ ]

for w in words: #เช่น ถ้า input = "Hello World" → words = ["Hello", "World"]
    '''
    ดังนั้น for w in words: หมายถึง

รอบแรก w = "Hello"

รอบสอง w = "World"'''
    ascii_values = [ ] # เก็บค่า ASCII ของแต่ละตัวอักษร
    for ch in w: # loop ทุกตัวในคำ
        ascii_values.append(str(ord(ch)))# แปลงเป็น ASCII แล้ว cast เป็น string
    result.append(" ".join(ascii_values))

print(" / ".join(result))


'''
for i in range(ord('a'), ord('z') + 1):
    print(f"{chr(i)} , {i}")

for i in range(ord('A'), ord('Z')+1):
    print(f"{chr(i)} , {i}")
'''