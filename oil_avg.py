volume = 50
list_1 = [ ]
list_2 = [ ]
# record 1
fuel1 = input("Fuel: ")
price1= float(input("Price: "))
km1 = float(input("KM: "))
list_1 = [fuel1, price1, km1]
avg_1 = price1*volume/km1
# record 2
fuel2 = input("Fuel: ")
price2 = float(input("Price: "))
km2 = float(input("KM: "))
list_2 = [fuel2, price2, km2]
avg_2 = price2*volume/km2
print(list_1)
print(list_2)
print(f'{avg_1:.2f}')
print(f'{avg_2:.2f}')

if avg_1 > avg_2:
    print(f"{fuel2} is cheaper than {fuel1}")
elif avg_1 < avg_2:
    print(f"{fuel1} is cheaper than {fuel2}")
else:
    print(f"{fuel1} and {fuel2} cost the same per km")
