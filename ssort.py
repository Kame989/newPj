s = input().strip()       # e.g. "3+5+1+8+9"

# 1) parse numbers (no split, only for-loops)
parts = []                # will hold number-strings like "124", "4634"
cur = ""
for ch in s:
    if ch == '+':
        parts.append(cur)
        cur = ""
    else: #ch is not +
        cur = cur + ch

# add the last number
if cur != "":
    parts.append(cur)

# 2) convert to integers (simple for-loop)
nums = []
for p in parts:
    nums.append(int(p))

# 3) selection sort (pure for-loops, no built-in sort)
n = len(nums)
for i in range(n):
    min_idx = i
    for j in range(i + 1, n):
        if nums[j] < nums[min_idx]:
            min_idx = j
    # swap
    nums[i], nums[min_idx] = nums[min_idx], nums[i]

# 4) join back into the required format
out = ""
for i in range(n):
    if i > 0:
        out = out + "+"
    out = out + str(nums[i])

print(out)
