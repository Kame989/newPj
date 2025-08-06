sc = int(input())

if int(sc) >100 :
    print("Error : Value must be less than or equal to 100.")
elif int(sc) < 0:
    print("Error : Value must be greater than or equal to 0.")
elif int(sc)  >= 90:
    print("A")
elif int(sc) >= 85:
    print("B+")
elif int(sc) >=80:
    print("B")
elif int(sc) >= 75:
    print("C+")
elif int(sc) >= 70:
    print("C")
elif int(sc) >= 65:
    print("D+")
elif int(sc) >= 60:
    print("D")
else:
    print("F")
