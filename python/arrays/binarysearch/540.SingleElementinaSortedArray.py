'''
540. Single Element in a Sorted Array
Solved
Medium

Topics
premium lock icon
Companies
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.

 

Example 1:

Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:

Input: nums = [3,3,7,7,10,11,11]
Output: 10
 

Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 105
'''

nums = [3,3,7,7,10,11,11]

n = len(nums) 
l,r = 0,n - 1

while l <= r :
    m = l + ((r - l)) // 2

    if m == 0 and nums[m + 1] != nums[m] :
        print(nums[m])
        break

    if m == n - 1 and nums[m - 1] != nums[m]:
        print(nums[m])
        break

    if nums[m - 1] != nums[m] != nums[m + 1] :  
        print(nums[m])
        break

    if m % 2 == 0 :
        if nums[m - 1] == nums[m] :
            r = m - 1
        else :
            l = m + 1
    else :
        if nums[m - 1] == nums[m] :
            l = m + 1
        else :
            r = m - 1
        

