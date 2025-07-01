'''
238. Product of Array Except Self
Solved
Medium

Topics
premium lock icon
Companies

Hint
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.
'''


#we can prefix and suffix arrays, then we can multiple them
# O(n)- time complexity
# O(n)- space complexity

nums = [-1,1,0,-3,3]
l = len(nums)

prefix = [1] * l
for i in range(1,l):
    prefix[i] = prefix[i-1] * nums[i-1]

suffix = [1] * l
for i in range(l-2,-1,-1):
    suffix[i] = suffix[i+1] * nums[i+1]

for i in range(l):
    nums[i] = prefix[i] * suffix[i]

print(nums)

# Instead of prefix and suffix arrays, we can calculate the values of prefix and suffix,
# then multiple them in res array

nums = [-1,1,0,-3,3]

l = len(nums)

res = [1] * l
for i in range(1,l):
    res[i] = res[i-1] * nums[i-1]

suffix = 1
for i in range(l-1,-1,-1):
    res[i] *= suffix
    suffix *= nums[i] 

print(res)