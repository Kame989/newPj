'''a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
sum= a+b+c+d+e
gpa = sum/5
print(f"THAI = {a}")
print(f"MATH = {b}")
print(f"ENGLISH = {c}")
print(f"SCIENCE = {d}")
print(f"SPORT = {e}")
print("---")
print(f"GPA = {gpa}")'''

#list of subjects
subs = ['T', 'E', 'C', 'S']

total = 0.0

for sub in subs:
    sc = float(input(f"enter {sub} score: "))
    total += sc
    print(f"{sub} = {sc:.2f}")


gp = total/len(subs)
print(f"gp = {gp}")

