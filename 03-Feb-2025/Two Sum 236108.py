# Problem: Two Sum - https://leetcode.com/problems/two-sum/description

class Solution(object):
    def twoSum(self, nums, target):
        if len(nums) <= 0:
            return False
        dictt = {}
        for i in range(len(nums)):
            if nums[i] in dictt:
                return dictt[nums[i]], i
            else:
                dictt[target - nums[i]] = i


        