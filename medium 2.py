def majority_element(nums):
    n = len(nums)
    
    # Dictionary to store the count of each element
    count_dict = {}

    # Iterate through the array and count the occurrences of each element
    for num in nums:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    # Find elements that appear more than ⌊ n/3 ⌋ times
    result = [key for key, value in count_dict.items() if value > n // 3]

    return result

# Get input from the user
nums = list(map(int, input("Enter the elements of the array separated by space: ").split()))

# Find and print elements that appear more than ⌊ n/3 ⌋ times
result = majority_element(nums)
print("Elements that appear more than ⌊ n/3 ⌋ times:", result)

#logic and algorithm of code

''' 
Function Definition (majority_element):
The function takes an array nums as an input parameter.

Getting the Length of the Array (n = len(nums)):
The length of the input array nums is stored in the variable n.

Counting Occurrences of Each Element (count_dict Dictionary):
A dictionary named count_dict is initialized to store the count of each element in the array.
The code iterates through the array using a for loop. For each element (num), it checks if the element is already a key in count_dict. 
If yes, it increments the count; otherwise, it adds the element to the dictionary with a count of 1.

Finding Elements that Appear More than ⌊ n/3 ⌋ Times (result List):
After counting the occurrences of each element, the code creates a list named result using a list comprehension.
The list contains elements (key) from the count_dict dictionary where the count (value) is greater than ⌊ n/3 ⌋.

Getting Input from the User (nums = list(map(int, input("Enter the elements of the array separated by space: ").split()))):
The user is prompted to enter space-separated elements for the array. The input is then converted to a list of integers using map and list.

Finding and Printing the Result (result = majority_element(nums) and print("Elements that appear more than ⌊ n/3 ⌋ times:", result)):
The majority_element function is called with the user-inputted array nums, and the result is stored in the variable result.
The elements that appear more than ⌊ n/3 ⌋ times are then printed as part of a formatted string.
'''

