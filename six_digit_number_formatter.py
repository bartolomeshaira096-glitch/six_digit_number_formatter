# Ask a user to input a number between 0 and 1000
number = input("Enter a number (0-1000):")
# Convert to string and add zeros at the beginning to make it 6 digits
formatted_number = number.zfill(6)
# Display the output