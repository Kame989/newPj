n = input()

digits =  [ ]
for ch in (n):
    digits.append(int(ch)) #convert ch str into int ch

print(digits)

print(type(digits))


total = 0
for d in digits: #loop each element/d in digitd
    total = total+d    #find total
print(total)

while total >=10:
    digit_sum = 0
    for ch in str(total): #go through each digit as str/ch
        digit_sum += int(ch)
    total = digit_sum

print(total)

'''n = input()

digits = [ ]
for ch in (n):
  digits.append(int(ch))
#print(digits)

total = 0

for item in (digits):
  total += item
#print(total)

while total >= 10 :
  sum = 0
  for ch in str(total):
    sum = sum + int(ch)
  total = sum
  #print(total)
  
print(total)'''