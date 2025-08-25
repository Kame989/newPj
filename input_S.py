n = input()
clear_n = ""

''' or use list comprehension
clear_n = "".join(ch for ch in n if ch.isdigit())
print(clear_n)
'''
for ch in n:
    if ch.isdigit():
        clear_n = clear_n + ch
    
print(clear_n)

