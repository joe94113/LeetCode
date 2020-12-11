# Given two binary trees and imagine that when you put one of them to cover the other,
# some nodes of the two trees are overlapped while the others are not.
#
#
# You need to merge them into a new binary tree. The merge rule is that if two nodes overlap,
# then sum node values up as the new value of the merged node.
# Otherwise, the NOT null node will be used as the node of new tree.

# Example 1:
#
# Input:
# 	Tree 1                     Tree 2
#           1                         2
#          / \                       / \
#         3   2                     1   3
#        /                           \   \
#       5                             4   7
# Output:
# Merged tree:
# 	     3
# 	    / \
# 	   4   5
# 	  / \   \
# 	 5   4   7


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# 遞迴解
# class Solution:
#     def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
#         if not t1 and not t2: return None
#         if not t1 or not t2: return t1 or t2
#         t1.val += t2.val
#         t1.left = self.mergeTrees(t1.left, t2.left)
#         t1.right = self.mergeTrees(t1.right, t2.right)
#         return t1





# 迭代解
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            return t2
        stack = []
        stack.append((t1, t2))
        while stack:
            t = stack.pop()
            if not t[1]:
                continue
            t[0].val += t[1].val
            print(t[0].val, '\n')
            if not t[0].left:
                t[0].left = t[1].left
            else:
                stack.append((t[0].left, t[1].left))
            if not t[0].right:
                t[0].right = t[1].right
            else:
                stack.append((t[0].right, t[1].right))
        return t1
