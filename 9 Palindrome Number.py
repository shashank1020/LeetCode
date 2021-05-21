#https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        i = 0
        while i<len(x):
            if (x[i] != x[~i]):
                return False
            i+=1
        return True

'''
Runtime: 64 ms, faster than 46.81% of Python3 online submissions for Palindrome Number.
Memory Usage: 14.1 MB, less than 91.81% of Python3 online submissions for Palindrome Number.
'''