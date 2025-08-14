from scipy import integrate
a = int(input())
b = int(input())

def f(x):
    return 3*x**2 + 2*x + 5

c =integrate.fixed_quad(f, a, b, n=2) [0]
print(int(c))

'''
F(b)−F(a)
f(x) = x**3+x**2+5x
แทน b & aใน x
f(b) = b**3+b**2+5b
f(a) = a**3+a**2+5a

a = int(input())
b = int(input())

c = (b**3 + b**2 + 5*b) - (a**3 + a**2 + 5*a)

print(c)

    
    '''