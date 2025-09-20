n =int(input())
hr = n//3600
left = n%3600
print(hr)
print(left)
m = left//60
s = left%60
print(m)
print(s)

print(f"{hr}:{m:02d}:{s:02d}")
