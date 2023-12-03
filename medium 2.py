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

