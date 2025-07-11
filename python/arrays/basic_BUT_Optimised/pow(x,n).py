'''
50. Pow(x, n)
Solved
Medium

Topics
premium lock icon
Companies
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

 

Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
 

Constraints:

-100.0 < x < 100.0
-231 <= n <= 231-1
n is an integer.
Either x is not zero or n > 0.
-104 <= xn <= 104
'''
# HERE THE CONSTRAINTS ARE COMPLICATED, THEY CAN 2 POWER 31 BUT WE CAN OPTIMISE UPTO ONLY 10 POWER 8.
'''
youtube link: https://youtu.be/WBzZCm46mFo?si=ZucV4C-tR3XPoezf
'''
x = 2.00000 
n = 10


if n < 0 :
    x = 1/x
    n = -n

binform = n
ans = 1

while binform > 0:
    if binform & 1 == 1:
        ans *= x
    x *= x
    binform >>= 1

print(ans)