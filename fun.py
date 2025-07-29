#กำหนดให้ f(n)=f(n-1)+100 เมื่อ n>0 และ f(0)=1
n = int(input())

res =1 + 100*n
if n <0:
  print("-1")
else:  
  print(res)