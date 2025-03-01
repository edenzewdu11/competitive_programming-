# Problem: Maximum Absolute Sum of Any Subarray - https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        maximum = nums[0]
        maxEnding = nums[0]
        for i in range(1, len(nums)):
            maxEnding = max(maxEnding + nums[i], nums[i])
            maximum = max(maximum, maxEnding)
            
        minimum=nums[0]
        minimumEnding=nums[0]
        for i in range(1,len(nums)):
            minimumEnding=min(minimumEnding+nums[i], nums[i])
            minimum=min(minimum,minimumEnding)
        ans=max(maximum,abs(minimum))
        return ans 
    
        
        