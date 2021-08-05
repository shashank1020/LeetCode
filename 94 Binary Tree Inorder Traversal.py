# https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self) -> None:
        self.inOrderList = []
        
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        if root:
            self.inorderTraversal(root.left)
            self.inOrderList += [root.val]
            self.inorderTraversal(root.right)
        return self.inOrderList


'''
Runtime: 28 ms, faster than 83.97% of Python3 online submissions for Binary Tree Inorder Traversal.
Memory Usage: 14 MB, less than 91.51% of Python3 online submissions for Binary Tree Inorder Traversal.
'''