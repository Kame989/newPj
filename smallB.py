'''n = input().split()
cl_n = ""

for ch in n:
    if ch.isalnum():
        cl_n = cl_n+ch

print(cl_n)'''


s = input()
clean_s = ""
for char in s:
    if char.isalnum():
        clean_s = clean_s+char
print(clean_s)

def count_case(s):
    up_count = 0
    low_count = 0
    for char in clean_s:
        if char.isupper():
            up_count = up_count+1
        elif char.islower():
            low_count = low_count+1
    return up_count,low_count

u,l = count_case(s)

print("UPPER:", u)
print("LOWER:", l)

    # Output: DataScienceRocks123
'''def clean_t(n):
    res = ""
    for char in n:
        if char.isalnum():
            res += char
    return res

def count_t(n):
    up_count = 0
    low_count = 0
    for char in n:
        if char.isupper():
            up_count += 1
        elif char.islower():
            low_count += 1
    return up_count, low_count   # return in the order you want to print

txt = input()
cleaned = clean_t(txt)
u, l = count_t(cleaned)

# remove the space using either sep="" or f-strings
print("UPPER:", u, sep="")   # -> UPPER:2
print("LOWER:", l, sep="")   # -> LOWER:5
# or:
# print(f"UPPER:{u}")
# print(f"LOWER:{l}")
    '''