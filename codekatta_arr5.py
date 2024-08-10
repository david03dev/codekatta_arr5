
def is_beautiful_array(nums):
    # Calculate the sum of the array
    total_sum = sum(nums)
    
    # Check if the total_sum is divisible by 2, 3, and 5
    if total_sum % 2 == 0 and total_sum % 3 == 0 and total_sum % 5 == 0:
        return 1
    else:
        return 0

# Read input
n = int(input())
array = list(map(int, input().split()))

# Output the result
print(is_beautiful_array(array))




"""
you are given with array of numbers.you have to find whether array is beautiful or not. A beautiful array is an array whose sum of all numbers is divisible by 2, 3 and 5

Input Description:
You are given a number ‘n’ denoting the size of array.Next line contains n space separated numbers.

Output Description:
Print 1 if array is beautiful and 0 if it is not

Sample Input :
5
5 25 35 -5 30

Sample Output :
1
"""
