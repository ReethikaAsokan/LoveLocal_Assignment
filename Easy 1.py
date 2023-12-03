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

#Logic and algorithm of the code

'''Function Definition (length_of_last_word):
The function takes a string s as an input parameter.

Splitting the String into Words (words = s.split()):
The split() method is used to break the input string s into a list of words based on spaces. 
This is done by splitting the string wherever a space character is encountered.
The resulting list of words is stored in the variable words.

Checking if There Are Any Words (if not words):
The code checks if the list of words is empty. If there are no words in the string, it means that the input string might be empty or only contains spaces. 
In such cases, the function returns 0 because there is no last word to determine the length.

Returning the Length of the Last Word (return len(words[-1])):
If there are words in the string, the function returns the length of the last word. 
It does this by accessing the last element of the list words using words[-1] and then calculating the length of that word using the len() function.

Getting Input from the User (s = input("Enter the string: ")):
The user is prompted to enter a string, and the input is stored in the variable s.

Calculating and Printing the Result (result = length_of_last_word(s) and print(f"The length of the last word is: {result}")):
The function length_of_last_word is called with the user-inputted string s, and the result is stored in the variable result.
The length of the last word is then printed as part of a formatted string. '''
