'''
74. Search a 2D Matrix
Solved
Medium

Topics
premium lock icon
Companies
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
'''


# matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
# target = 3

# rows, columns = len(matrix), len(matrix[0])

# def bs(nums, target) :
#     l, r = 0, len(nums) - 1

#     while l <= r :
        
#         m = l + (r - l) // 2
#         if nums[m] == target :
#             return True
#         elif nums[m] > target :
#             r = m - 1
#         else :
#             l = m + 1

#     return False
# l, r = 0, rows - 1
# flag = True

# while l <= r :

#     m = l + (r - l) // 2

#     if matrix[m][0] <= target <= matrix[m][columns - 1]:
#         print(bs(matrix[m],target))
#         flag = False
#         break
#     elif matrix[m][0] > target :
#         r = m - 1
#     else :
#         l = m + 1

# if flag : print(False)


matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 0

rows, colums = len(matrix), len(matrix[0])

def binarySearch(nums) :
    l, r = 0, len(nums) - 1 

    while l <= r :
        m = l + (r - l) // 2

        if nums[m] == target :
            return True
        elif nums[m] > target :
            r = m - 1
        else :
            l = m + 1
    return False

l, r = 0, rows - 1 
flag = True
while l <= r :
    m = l + (r - l) // 2

    if matrix[m][0] <= target <= matrix[m][colums - 1] :
        print(binarySearch(matrix[m])) 
        flag = False
        break
    elif matrix[m][0] > target :
        r = m - 1 
    else :
        l = m + 1
if flag : print(False)