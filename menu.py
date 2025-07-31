d = input().strip().lower()
m = input().strip().lower()
b = input().strip().lower()
s = input().strip().lower()

choices = [d, m, b, s]

chix_count = choices.count("chicken rice")
nood_count = choices.count("noodle")
if chix_count > nood_count:
    win = "Chicken Rice"
elif chix_count < nood_count:
    win = "Noodle"
else :
    win = s

print(win.capitalize())  # Capitalize the first letter of the winning dish
#print(*choices)  # Print all choices separated by space