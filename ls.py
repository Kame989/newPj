list1 = []
list2 = []
list3 = []

list1_str = input("enter: ")
list1 = list1_str.split()
set1 = set(list1)
list2_str = input("enter: ")
list2 = list2_str.split()
set2 = set(list2)
list3_str = input("enter: ")
list3 = list3_str.split()
set3 = set(list3)
print("list1: ", list1)
print("list2: ", list2)
print("set1:", set1)
print("set2:", set2)
intersect = list(set1 & set2)
inter_set = set1.intersection(set2)
print("intersect:", *intersect)
diff = list(inter_set - set3)
if not diff:
    print("No difference found")
else:
    print("diff:", *diff)
