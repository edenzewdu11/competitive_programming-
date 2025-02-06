# Problem: Apply Operations to an Array - https://leetcode.com/problems/apply-operations-to-an-array/

class Solution(object):
    def applyOperations(self, nums):
        arr = []
        arr_zero = []

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] = nums[i] * 2
                nums[i + 1] = 0

        for num in nums:
            if num != 0:
                arr.append(num)
            else:
                arr_zero.append(num)

        arr.extend(arr_zero)

        return arr
