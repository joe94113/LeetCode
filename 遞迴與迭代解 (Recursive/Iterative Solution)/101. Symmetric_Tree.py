# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
#
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
#
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left


# 遞迴解
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        return self.isSym(root.left, root.right)

    def isSym(self, l: TreeNode, r: TreeNode) -> bool:
        if not l and not r: return True
        if not l or not r: return False
        if l.val != r.val: return False
        return self.isSym(l.left, r.right) and self.isSym(l.right, r.left)
