
n = input()

count = 0

for char in n:
    if char.isalnum( ) : # Checks if the character is alphanumeric (letter or number)
        count += 1
    
print(count)
