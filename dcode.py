# read the string
s = input().strip()            # example: myoxjmvle

# read the line with numbers (like: [8, 3, 7, 9]  or  8 3 7 9  or 8,3,7,9)
line = input().strip()

# remove brackets and commas, then split into pieces
line = line.replace('[', '').replace(']', '').replace(',', ' ')
parts = line.split()          # now parts is like ['8', '3', '7', '9']

print(type(parts))
print(line)
# convert parts to integers

nums = []
for p in line:
    nums.append(int(p))

print(nums)

aws  = ' '
for n in nums:
    if 1 <= n <= len(s):
        aws = aws + s[n-1]

print(aws)

'''
Humans usually say the 1st letter, 2nd letter, … — that’s 1-based counting.
Python uses 0-based indexes, so the first letter is s[0], the second is s[1], etc.

If you want the n-th letter from human counting, you must use s[n-1] in Python (because Python starts at 0).'''