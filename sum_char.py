n = input().upper()
total = 0


for char in n:
    if char.isalpha():
        total = total + (ord(char) - ord('A')+1)


print(total)

