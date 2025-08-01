'''def print_primes_up_to_100():
    # 1. Check every number x from 2 to 100
    for x in range(2, 101):
        # 2. Try dividing x by every y from 2 up to x-1
        for y in range(2, x):
            if x % y == 0:
                # x is divisible by y → not prime, stop checking further
                break
        else:
            # The else on the for-loop runs only if we never hit 'break'
            # which means x had no divisors → x is prime!
            print(x)

print("Primes from 2 to 100:")
print_primes_up_to_100()
'''
my_num = int(input("Enter a number: "))
count =0
for num in range (2, my_num+1):
    for i in range(2, num):
        if num % i ==0:
            # not prime, so we can stop checking further
            break
    else:
        # if we never hit 'break', num is prime
        count += 1

print(f"{count} of prime")    

'''
my_num = int(input())
count = 0

if my_num <= 0:
  print("ไม่สามารถหาได้")
else:
  for num in range(2, my_num+1):
    for i in range(2, num):
      if num % i == 0:
      #print("not prime")
        break
      
    else:
      count += 1

#print(f"there are {count} of my_num")
  print(f"จำนวนเฉพาะในช่วง 0 ถึง {my_num}")
  print(f"มีอยู่ {count} จำนวน")'''