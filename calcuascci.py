n = input()
#ascii_v = ord(n)
ascii_list = [ ]
for char in n:
    ascii_list.append(int(ord(char)))

#print(ascii_v)
print(ascii_list)

re = 0
for ch in range(len(ascii_list)):
    re = re + ascii_list[ch]
print(re)