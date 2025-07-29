nums = [int(x) for x in input().split(',')]
'''In Python, the square brackets around a comprehension are what 
tell the interpreter “build me a list of these values.”

or use this code same result

parts = input().split(',')       # e.g. ["1","2","3"]
nums = []
for x in parts:
    nums.append(int(x))

'''
res = [n for n in nums if n == 1 or (n % 7 == 0 and n% 11 != 0)]

print(','.join(map(str,res)) or 'none')