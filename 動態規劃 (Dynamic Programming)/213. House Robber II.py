# You are a professional robber planning to rob houses along a street.
# Each house has a certain amount of money stashed. All houses at this place are arranged in a circle.
# That means the first house is the neighbor of the last one. Meanwhile,
# adjacent houses have a security system connected,
# and it will automatically contact the police if two adjacent houses were broken into on the same night.
#
# Given a list of non-negative integers nums representing the amount of money of each house,
# return the maximum amount of money you can rob tonight without alerting the police.
#
# Example 1:
#
# Input: nums = [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
# Example 2:
#
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.


# class Solution:
#     def rob(self, nums):
#         def rob(nums):
#             now = prev = 0
#             for n in nums:
#                 now, prev = max(now, prev + n), now
#             return now
#         return max(rob(nums[len(nums) != 1:]), rob(nums[:-1]))


class Solution:
    def rob(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 0:
            return 0
        if l == 1:
            return nums[0]

        # don't rob 0 first -> res = rob[l-1]
        # rob[i] = max(nums[i] + rob[i-2], rob[i-1])
        pre, cur = 0, nums[1]
        for i in range(2, l):
            tmp, pre = pre, cur
            cur = max(nums[i] + tmp, pre)
            print(cur)
        res = cur

        # rob 0 -> res = rob[l-2]
        pre, cur = nums[0], nums[0]
        for i in range(2, l - 1):
            tmp, pre = pre, cur
            cur = max(nums[i] + tmp, pre)
            print(cur)
        return max(res, cur)