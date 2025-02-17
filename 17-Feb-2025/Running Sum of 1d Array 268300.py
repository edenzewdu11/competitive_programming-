# Problem: Running Sum of 1d Array - https://leetcode.com/problems/running-sum-of-1d-array/

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        acc=0
        prefix_sum=[0]*len(nums)
        for i in range(len(nums)):
            acc+=nums[i]
            prefix_sum[i]=acc
        return prefix_sum

            
        