# Prompt the user for a positive integer input
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use a while loop for each row
while row < size:
    # For loop to print asterisks side by side in a row
    for col in range(size):
        print("*", end="")
    # Move to the next line after printing each row
    print()
    # Increment row counter
    row += 1
