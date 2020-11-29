# Given a sorted array of distinct integers and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.
# Example :
#
# Input: nums = [1,3,5,6], target = 5
# Output: 2
from typing import List

nums = [1, 3, 5, 6]
target = 5
self = None

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mi = (hi + lo) // 2
            if nums[mi] == target:
                return mi
            elif nums[mi] > target:
                hi = mi - 1
            else:
                lo = mi + 1
        return lo

print(Solution.searchInsert(self, nums, target))
