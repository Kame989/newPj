a = int(input())
b = int(input())

a_pow = pow(a,2)
b_pow = pow(b,2)

plus  = a_pow + 2*(a*b) + b_pow
minu = a_pow - 2*a*b + b_pow
print(plus)
print(minu)