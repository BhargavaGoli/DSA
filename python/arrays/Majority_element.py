'''
169. Majority Element
Solved
Easy

Topics
premium lock icon
Companies
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2 
'''

#Brute_Force-O(n^2)
nums=[2,2,1,1,1,2,2]
n=len(nums)//2
for i in nums:
    freq=0
    for j in nums:
        if i == j:
            freq += 1
    if freq > n:
        print(i)
        break

# Boyer-Moore Voting Algorithm -- O(n)

freq=0
ele=None

for i in nums:
    if freq == 0 :
        ele=i
    freq += 1 if ele == i else -1

print(ele)