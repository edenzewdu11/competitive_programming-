# Problem: Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        answer = []

        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]
        
        for i in range(len(nums)-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]
        
        for i in range(len(nums)):
            answer.append(prefix[i] * suffix[i])
        return answer
