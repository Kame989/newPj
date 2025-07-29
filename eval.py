import ast


# อ่าน input เช่น "[5, 50, 500]"
nums = ast.literal_eval(input())

# หาและพิมพ์ค่าสูงสุด
print(max(nums))


'''or
data = input().strip()    # อ่าน "[10, 20, 30, 40]"
data = data[1:-1]         # ตัด [ ] ออก → "10, 20, 30, 40"
nums = [int(x) for x in data.split(',') if x.strip()]

print(max(nums))

'''

