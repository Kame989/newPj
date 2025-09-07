n1 = input()
y1 = int(input())
n2 = input()
y2 = int(input())
n3 = input()
y3 = int(input())

if y1 > y2 and y1 > y3:
    print(f'{n1} is older than {n2}')
    print(f'{n2} is older than {n3}')
    print(f'{n1} is older than {n3}')
else:
    print(f'{n1} is older than {n2}')
    print(f'{n1} and {n2}would be sibling')
    print(f'{n1} is older than {n2}')

