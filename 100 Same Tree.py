# https://leetcode.com/problems/same-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p and q:
            if p.val == q.val:
                if self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right):
                    return True
                else:
                    return False
            else: 
                return False
        elif not p and not q:
            return True
        else:
            return False


'''
Runtime: 24 ms, faster than 95.38% of Python3 online submissions for Same Tree.
Memory Usage: 14.3 MB, less than 31.38% of Python3 online submissions for Same Tree.
'''