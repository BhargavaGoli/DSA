'''
567. Permutation in String
Solved
Medium

Hint
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 

Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
'''

from collections import Counter

s1 = "ab"
s2 = "eidbaooo"

l1, l2 = len(s1), len(s2)

count = Counter(s1)
flag = True

for i in range(l2 - l1 + 1) :
    if count == Counter(s2[i : i + l1]) :
        print(True)
        flag = False
        break
if flag :
    print(False)