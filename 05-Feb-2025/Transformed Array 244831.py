# Problem: Transformed Array - https://leetcode.com/problems/transformed-array/description/

class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        
        for i in range(n):
            if nums[i] > 0:
                new = (i + nums[i]) % n
                result[i] = nums[new]
            elif nums[i] < 0:
                new = (i + nums[i]) % n
                result[i] = nums[new]
            else:
                result[i] = 0
        
        return result
