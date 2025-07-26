'''
18. 4Sum
Solved
Medium

Topics
premium lock icon
Companies
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

 

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
 

Constraints:

1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109
'''

nums = [1,0,-1,0,-2,2]
target = 0 

#sort the list
nums.sort()
n = len(nums) 

result = list()

for i in range(n - 3) :
    #optimize case 1 by removing i duplicates
    if i > 0 and nums[i - 1] == nums[i] : continue

    for j in range(i + 1, n - 2) :
        if j > i + 1 and nums[j - 1] == nums[j] : continue

        k, l = j + 1, n - 1
        while k < l :
            total = nums[i] + nums[j] + nums[k] + nums[l]
            if total < target :
                k += 1
            elif total > target :
                l -= 1
            else : # total == target 
                result.append([nums[i], nums[j], nums[k], nums[l]])
                k += 1
                l -= 1
                while k < l and nums[k - 1] == nums[k] : k +=1 

print(result)