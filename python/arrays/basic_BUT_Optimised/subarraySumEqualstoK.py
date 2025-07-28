'''
560. Subarray Sum Equals K
Solved
Medium

Topics
premium lock icon
Companies

Hint
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
 

Constraints:

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107
'''

#Brute-force solution

def brutesub(nums, k) :
    n = len(nums)
    count = 0 
    for i in range(n) :
        for j in range(i, n) :
            if sum(nums[i : j + 1]) == k :
                count += 1
        
    return count

#optimized 

def subarraySumEqualstoK(nums, k ) :
    n = len(nums)
    result = {}
    result[0] = 1
    prefixsum = count = 0

    for i in nums :
        prefixsum += i 

        if prefixsum - k in result :
            count += result[prefixsum - k]

        result[prefixsum] = result.get(prefixsum, 0) + 1 

    return count 

if __name__ == "__main__" :
    nums = [1,2,3]
    k = 3
    print(subarraySumEqualstoK(nums, k))