'''
410. Split Array Largest Sum
Solved
Hard

Topics
premium lock icon
Companies
Given an integer array nums and an integer k, split nums into k non-empty subarrays such that the largest sum of any subarray is minimized.

Return the minimized largest sum of the split.

A subarray is a contiguous part of the array.

 

Example 1:

Input: nums = [7,2,5,10,8], k = 2
Output: 18
Explanation: There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8], where the largest sum among the two subarrays is only 18.
Example 2:

Input: nums = [1,2,3,4,5], k = 2
Output: 9
Explanation: There are four ways to split nums into two subarrays.
The best way is to split it into [1,2,3] and [4,5], where the largest sum among the two subarrays is only 9.
 

Constraints:

1 <= nums.length <= 1000
0 <= nums[i] <= 106
1 <= k <= min(50, nums.length)
'''

def isValid(m,nums,k):
    stu,pages = 1,0

    for i in nums:
        if i > m :
            return False
        
        if pages + i <= m :
            pages += i
        else :
            stu += 1
            pages = i
    return True if stu <= k else False 

nums = [7,2,5,10,8]
k = 2

ans = None
l,r = max(nums),sum(nums)

while l <= r :
    m = l + (r - l) // 2

    if isValid(m,nums,k):
        ans = m
        r = m - 1
    else :
        l = m + 1

print(ans)