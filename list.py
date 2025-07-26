numbers = [ ]  # Initialize an empty list to store the numbers

while True:
    user_input = input("Enter a number (or type '0' to finish): ")
    if user_input ==0:
        break  # Exit the loop if the user types 'done'
    try:
        number = int(user_input)  # Convert input to a float
        numbers.append(number)  # Add the number to the list
    except ValueError:
        print("Invalid input. ")

if numbers:  # Check if the list is not empty
    minimum_value = min(numbers)
    maximum_value = max(numbers)
    print(f"The minimum value entered is: {minimum_value}")
    print(f"The maximum value entered is: {maximum_value}")
else:
    print("No numbers were entered.")