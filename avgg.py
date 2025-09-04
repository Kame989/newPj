total = 0 
count = 0
while True:
    n = int(input())
    if n ==-1:
        break
    total = total + n
    count = count + 1

print(total)

if count > 0:
    avg = total / count
    print(f'{avg:.2f}')
else:
    print('0.00')

