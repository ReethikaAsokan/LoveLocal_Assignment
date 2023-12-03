def length_of_last_word(s):
    # Split the input string into words using spaces as the delimiter
    words = s.split()

    # Check if there are any words in the string
    if not words:
        return 0

    # Return the length of the last word
    return len(words[-1])

# Get input from the user
s = input("Enter the string: ")

# Calculate and print the length of the last word
result = length_of_last_word(s)
print(f"The length of the last word is: {result}")