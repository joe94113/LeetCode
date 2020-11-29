# Given two strings s and t , write a function to determine if t is an anagram of s.
#
# Example :
#
# Input: s = "anagram", t = "nagaram"
# Output: true


# 簡化之解
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        cnt = {}
        for c in s:
            cnt[c] = cnt.get(c, 0) + 1
        for c in t:
            if c not in cnt or cnt[c] == 0:
                return False
            else:
                cnt[c] -= 1
        return True


# 用套件解
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         from collections import Counter
#         Counter(s) == Counter(t)


# 自己解
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False
#         else:
#             tdict = {}
#             sdict = {}
#             for i in s:
#                 if i not in sdict:
#                     sdict[i] = 1
#                 else:
#                     sdict[i] = sdict[i] + 1
#             for i in t:
#                 if i not in tdict:
#                     tdict[i] = 1
#                 else:
#                     tdict[i] = tdict[i] + 1
#             return(sdict == tdict)
