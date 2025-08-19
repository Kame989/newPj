n = input()
line = n.strip()
m_list = [ ]

print(n)
print(line)

is_p = " "

for ch in line:
    if ch == "+":
        m_list.append(is_p)
        is_p = " "
    else: #ch is not +
        is_p = is_p + ch

if is_p != " ":
    m_list.append(is_p)

nums = [ ]
for ele in m_list: #convert to int
    nums.append(int(ele))

n = len(nums)

for i in range (n):
    min_ind = i
    for j in range(i+1, n):
        if nums[j] < nums[min_ind]:
            min_ind = j

nums[i], nums[min_ind] = nums[min_ind], nums[i]

out = ""
for i in range(n):
    if i > 0:
        out = out + "+"
    out = out + str(nums[i])

print(out)
