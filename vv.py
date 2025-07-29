list_a = ["red", "green", "blue", "yellow"]
list_b = ["green", "purple", "red"]

    # Using set difference
unique_to_a = list(set(list_a) - set(list_b))
print(f"Elements in list_a but not list_b: {unique_to_a}")