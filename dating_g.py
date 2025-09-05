n = int(input())
n_list = [ ]
for i in range(n):
    name, money = input().split()
    money = int(money)
    n_list.append((name, money))

budget = int(input())

ar_name = sorted(n_list, reverse=True)

print(ar_name)
total = 0
for girl in n_list:
    total = total + girl[1]
    if budget >= total:
        print({girl[0]})



