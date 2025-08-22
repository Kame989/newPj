Amount = int(input())
gradeList = [ ]

for i in range(Amount):
    x = int(input())
    if x > 100 or x < 0: 
        gradeList.append('Invalid Grade')
    elif x >= 80: 
        gradeList.append('A')
    elif x >= 70: 
        gradeList.append('B')
    elif x >= 60: 
        gradeList.append('C')
    elif x >= 50: 
        gradeList.append('D')
    else: 
        gradeList.append('F')

for i in gradeList:
    print(i)