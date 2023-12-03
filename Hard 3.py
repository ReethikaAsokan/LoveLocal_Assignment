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
