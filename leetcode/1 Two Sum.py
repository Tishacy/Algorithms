"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
class Solution(object):
    # Approach 1: Brute Force
    def twoSum1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, a in enumerate(nums):
            for j, b in enumerate(nums[i+1:]):
                if a + b == target:
                    return [i, j+i+1]

    # Approach 2: Two-pass Hash Table
    def twoSum2(self, nums, target):
        for i, a in enumerate(nums):
            b = target - a
            if (b in nums) and (nums.index(b) != i):
                return [i, nums.index(b)]

    # Approach 3: One-pass Hash Table
    def twoSum3(self, nums, target):
        buffer_dict = {}
        for i, a in enumerate(nums):
            if a in buffer_dict:
                return [buffer_dict[a], i]
            else:
                buffer_dict[target - a] = i

if __name__=="__main__":
    nums = [2, 7, 11, 15]
    target = 9
    s = Solution().twoSum3(nums, target)
    print(s)
