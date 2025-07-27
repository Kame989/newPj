data = input().strip()        # ex: "[5, 50, 500]"
data = data[1:-1]             # ตัด [ ] ออก -> "5, 50, 500"
nums = [int(x) for x in data.split(',')]
print(max(nums))
