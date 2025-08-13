'''
link : https://www.geeksforgeeks.org/problems/rat-in-a-maze-problem/1&selectedLang=python3

Rat in a Maze Problem - I
Difficulty: MediumAccuracy: 35.75%Submissions: 363K+Points: 4Average Time: 25m
Consider a rat placed at position (0, 0) in an n x n square matrix mat[][]. The rat's goal is to reach the destination at position (n-1, n-1). The rat can move in four possible directions: 'U'(up), 'D'(down), 'L' (left), 'R' (right).

The matrix contains only two possible values:

0: A blocked cell through which the rat cannot travel.
1: A free cell that the rat can pass through.
Your task is to find all possible paths the rat can take to reach the destination, starting from (0, 0) and ending at (n-1, n-1), under the condition that the rat cannot revisit any cell along the same path. Furthermore, the rat can only move to adjacent cells that are within the bounds of the matrix and not blocked.
If no path exists, return an empty list.

Note: Return the final result vector in lexicographically smallest order.

Examples:

Input: mat[][] = [[1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]]
Output: ["DDRDRR", "DRDDRR"]
Explanation: The rat can reach the destination at (3, 3) from (0, 0) by two paths - DRDDRR and DDRDRR, when printed in sorted order we get DDRDRR DRDDRR.
Input: mat[][] = [[1, 0], [1, 0]]
Output: []
Explanation: No path exists as the destination cell is blocked.
Input: mat = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
Output: ["DDRR", "RRDD"]
Explanation: The rat has two possible paths to reach the destination: 1. "DDRR" 2. "RRDD", These are returned in lexicographically sorted order.
Constraints:
2 ≤ mat.size() ≤ 5
0 ≤ mat[i][j] ≤ 1

'''

class Solution :
    def findPath(self, maze) :
        n = len(maze) 
        result = []

        def backtrack(row, col, path) :
            
            if row < 0 or row >= n or col < 0 or col >= n or maze[row][col] != 1 :
                return 
            
            if row == n - 1 and col == n - 1 :
                result.append(path)
                return 
            
            maze[row][col] = -1

            backtrack(row + 1, col, path + "D") # Down
            backtrack(row, col - 1, path + "L" ) # left
            backtrack(row, col + 1, path + "R") # right 
            backtrack(row - 1, col, path + "U") # up

            maze[row][col] = 1
        
        backtrack(0, 0, "")
        return result

if __name__ == "__main__" :
    s = Solution()
    maze = [[1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]]
    result = s.findPath(maze)
    print(result)