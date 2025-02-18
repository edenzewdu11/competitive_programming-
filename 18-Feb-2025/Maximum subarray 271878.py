# Problem: Maximum subarray - https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = nums[0]
        maxEnding = nums[0]

        for i in range(1, len(nums)):
       
            maxEnding = max(maxEnding + nums[i], nums[i])
        
       
            maximum = max(maximum, maxEnding)
    
        return maximum

        