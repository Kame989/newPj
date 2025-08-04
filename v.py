import math
t = float(input())

v = 144 / t
v = math.ceil(v*100)/100

'''In our rounding-up code

python
Copy code
v = 144 / t         # e.g., v = 44.3077…
# math.ceil(v * 100) makes 44.3077*100 = 4430.77 → ceiling → 4431
# then divide by 100 → 44.31
v_rounded_up = math.ceil(v * 100) / 100
'''

print(f"{v:.2f} km/hr")