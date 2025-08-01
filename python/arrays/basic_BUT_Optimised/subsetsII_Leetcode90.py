'''
90. Subsets II
Solved
Medium

Topics
premium lock icon
Companies
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
'''

nums = [1,2,2]

#backtracking neatly explained
result = []

def backtrack(subset, i) :
    if i == len(nums) :
        result.append(subset[:])
        return
    #include
    subset.append(nums[i])
    backtrack(subset, i + 1)
    #exclude
    subset.pop()
    
    while i + 1 < len(nums) and nums[i + 1] == nums[i] :
        i += 1

    backtrack(subset, i + 1)
backtrack([], 0)
print(result)

#backtracking with loop
result = []

def backtrack(subset, start) :
    result.append(subset[:])

    for i in range(start, len(nums)) :
        if i > start and nums[i - 1] == nums[i] :
            continue 

        subset.append(nums[i])
        backtrack(subset, i + 1)
        #exclude
        subset.pop()

backtrack([], 0)


print(result)