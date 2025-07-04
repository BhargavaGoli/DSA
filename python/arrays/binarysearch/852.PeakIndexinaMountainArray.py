'''
852. Peak Index in a Mountain Array
Solved
Medium

Topics
premium lock icon
Companies
You are given an integer mountain array arr of length n where the values increase to a peak element and then decrease.

Return the index of the peak element.

Your task is to solve it in O(log(n)) time complexity.

 

Example 1:

Input: arr = [0,1,0]

Output: 1

Example 2:

Input: arr = [0,2,1,0]

Output: 1

Example 3:

Input: arr = [0,10,5,2]

Output: 1

 

Constraints:

3 <= arr.length <= 105
0 <= arr[i] <= 106
arr is guaranteed to be a mountain array.
'''

nums = [0,5,10,2]


l,r = 1,len(nums) - 2

while l <= r :

    m = l + (r-l) // 2

    if nums[m - 1] < nums[m] > nums[m + 1] :
        print(m)
        break
    elif nums[m - 1] < nums[m] :
        l = m + 1
    else :
        r = m - 1

      