'''
15. 3Sum
Solved
Medium

Topics
premium lock icon
Companies

Hint
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105
'''

nums = [-1,0,1,2,-1,-4]

#sort the list
nums.sort()
n = len(nums)
target = 0 
result = list()

for i in range(n - 2) :
    if i > 0 and nums[i - 1] == nums[i] : continue
    p, q = i + 1, n - 1
    while p < q :
        total = nums[i] + nums[p] + nums[q] 
        if total < target :
            p += 1
        elif total > target :
            q -= 1
        else : # total == target
            result.append([nums[i],nums[p],nums[q]])
            p += 1
            q -= 1
            while p < q and nums[p - 1] == nums[p] : p += 1
                
print(result)