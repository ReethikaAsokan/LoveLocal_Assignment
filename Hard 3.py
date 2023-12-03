def count_digit_one(n):
    count = 0
    
    # Iterate through each digit place from right to left
    for i in range(1, n + 1):
        # Convert the current number to a string to count '1's
        count += str(i).count('1')
    
    return count

# Get input from the user
n = int(input("Enter the value of n: "))

# Count and print the total number of digit 1
result = count_digit_one(n)
print("Total number of digit 1 appearing in all non-negative integers up to", n, "is:", result)

#logic and algorithm

'''
Function Definition (count_digit_one):
The function takes an integer n as an input parameter.

Initialization (count = 0):
A variable named count is initialized to store the total count of digit 1.

Iterating through Each Digit Place (for i in range(1, n + 1):):
The code uses a for loop to iterate through each number from 1 to n (inclusive).
For each number (i), it converts the number to a string using str(i) to facilitate counting the occurrences of the digit '1'.

Counting Digit 1 (count += str(i).count('1')):
For each number (i), the code counts the occurrences of the digit '1' in its string representation using the count() method for strings.
The count is then added to the count variable.

Returning the Total Count (return count):
After iterating through all the numbers, the function returns the total count of digit 1.

Getting Input from the User (n = int(input("Enter the value of n: "))):
The user is prompted to enter the value of n, and the input is converted to an integer.

Counting and Printing the Result (result = count_digit_one(n) and print("Total number of digit 1 appearing in all non-negative integers up to", n, "is:", result)):
The count_digit_one function is called with the user-inputted value of n, and the result is stored in the variable result.
The total number of digit 1 is then printed as part of a formatted string.
'''
