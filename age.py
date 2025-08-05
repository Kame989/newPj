ages = input().split() #str

num = [ ]

#convert age to int in loop
for i in ages: #let i run = as much time as u type in age eg, 2  1 3 = 3times
    num.append(int(i)) # adding age in the num list

n, m, y  = num #unpack or put the value in each variable orderly


a = y -((n*m)/(1-m))
b =y -(n/(1-m))

print(f"{int(a)} {int(b)}")