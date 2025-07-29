list1 = ["red", "green", "blue"]
list2 = ["yellow", "pink", "blue"]
list3 = ["blue", "green", "purple"]     
# Convert lists to sets
set1 = set(list1)
set2 = set(list2)
set3 = set(list3)   
# Find the intersection using the '&' operator or .intersection() method
intersection_set = set1 & set2
# Alternatively: intersection_set = set1.intersection(set2)
difference_set = intersection_set - set3
# Convert the resulting set back to a list if needed
intersection_list = list(intersection_set)
difference_list = list(difference_set)

print(*intersection_list)
print("*******")
print("diff:", *difference_list)
